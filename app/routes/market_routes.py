"""
Market Routes
=============
Routes for market analysis and opportunity scanning.
"""

from flask import Blueprint, render_template, jsonify
from app.models.models import Settings, Portfolio
from app.services import market_service, price_service

bp = Blueprint('market', __name__)


@bp.route('/market')
def market_page():
    """Render the market analysis page."""
    return render_template('market.html')


@bp.route('/api/market/analysis')
def market_analysis():
    """Get comprehensive market analysis data."""
    settings = Settings.query.first()
    if not settings:
        return jsonify({
            'success': False,
            'error': 'No settings configured. Please configure settings first.'
        }), 404
    
    # Get market status for primary index
    market_status = market_service.get_market_status(settings.index_ticker)
    
    if not market_status:
        return jsonify({
            'success': False,
            'error': 'Could not fetch market data'
        }), 500
    
    # Get thresholds for display
    thresholds = {
        'mild_dip': settings.threshold_mild_dip,
        'correction': settings.threshold_correction,
        'bear': settings.threshold_bear,
        'crash': settings.threshold_crash
    }
    
    # Get multipliers
    multipliers = {
        'normal': settings.multiplier_normal,
        'mild_dip': settings.multiplier_mild_dip,
        'correction': settings.multiplier_correction,
        'bear': settings.multiplier_bear,
        'crash': settings.multiplier_crash
    }
    
    # Get current multiplier based on condition
    condition = market_status.get('condition', 'normal')
    current_multiplier = multipliers.get(condition, 1.0)
    
    return jsonify({
        'success': True,
        'data': {
            'index_ticker': settings.index_ticker,
            'current_price': market_status.get('current_price', 0),
            'ath_price': market_status.get('ath', 0),
            'drawdown_percent': market_status.get('drawdown_percent', 0),
            'condition': condition,
            'condition_display': market_status.get('condition_display', 'Unknown'),
            'current_multiplier': current_multiplier,
            'base_investment': settings.base_investment,
            'adjusted_investment': settings.base_investment * current_multiplier,
            'thresholds': thresholds,
            'multipliers': multipliers
        }
    })


@bp.route('/api/market/opportunities')
def market_opportunities():
    """Scan portfolio for buying opportunities based on individual stock dips."""
    portfolio = Portfolio.query.first()
    if not portfolio or not portfolio.holdings:
        return jsonify({
            'success': False,
            'error': 'No portfolio configured'
        }), 404
    
    settings = Settings.query.first()
    if not settings:
        return jsonify({
            'success': False,
            'error': 'No settings configured'
        }), 404
    
    opportunities = []
    
    for holding in portfolio.holdings:
        # Get stock data with 52-week high
        stock_data = market_service.get_stock_analysis(holding.ticker)
        if not stock_data:
            continue
        
        current_price = stock_data.get('current_price', 0)
        high_52w = stock_data.get('high_52w', 0)
        
        if high_52w > 0 and current_price > 0:
            drawdown = ((high_52w - current_price) / high_52w) * 100
            
            # Determine opportunity level
            opportunity_level = 'none'
            opportunity_score = 0
            
            if drawdown >= 30:
                opportunity_level = 'exceptional'
                opportunity_score = 5
            elif drawdown >= 20:
                opportunity_level = 'strong'
                opportunity_score = 4
            elif drawdown >= 10:
                opportunity_level = 'moderate'
                opportunity_score = 3
            elif drawdown >= 5:
                opportunity_level = 'mild'
                opportunity_score = 2
            else:
                opportunity_level = 'none'
                opportunity_score = 1
            
            opportunities.append({
                'ticker': holding.ticker,
                'name': holding.name,
                'target_allocation': holding.target_allocation,
                'current_price': round(current_price, 2),
                'high_52w': round(high_52w, 2),
                'drawdown_percent': round(drawdown, 2),
                'opportunity_level': opportunity_level,
                'opportunity_score': opportunity_score,
                'change_24h': stock_data.get('change_percent', 0)
            })
    
    # Sort by opportunity score (highest first), then by drawdown
    opportunities.sort(key=lambda x: (-x['opportunity_score'], -x['drawdown_percent']))
    
    # Calculate summary
    total_opportunities = len([o for o in opportunities if o['opportunity_score'] >= 3])
    avg_drawdown = sum(o['drawdown_percent'] for o in opportunities) / len(opportunities) if opportunities else 0
    
    return jsonify({
        'success': True,
        'data': {
            'opportunities': opportunities,
            'summary': {
                'total_stocks': len(opportunities),
                'buying_opportunities': total_opportunities,
                'average_drawdown': round(avg_drawdown, 2)
            }
        }
    })


@bp.route('/api/market/condition-meter')
def condition_meter():
    """Get data for the market condition meter visualization."""
    settings = Settings.query.first()
    if not settings:
        return jsonify({
            'success': False,
            'error': 'No settings configured'
        }), 404
    
    market_status = market_service.get_market_status(settings.index_ticker)
    if not market_status:
        return jsonify({
            'success': False,
            'error': 'Could not fetch market data'
        }), 500
    
    drawdown = market_status.get('drawdown_percent', 0)
    
    # Define zones for the meter
    zones = [
        {'name': 'Normal', 'min': 0, 'max': settings.threshold_mild_dip, 'color': '#10B981', 'multiplier': settings.multiplier_normal},
        {'name': 'Mild Dip', 'min': settings.threshold_mild_dip, 'max': settings.threshold_correction, 'color': '#3B82F6', 'multiplier': settings.multiplier_mild_dip},
        {'name': 'Correction', 'min': settings.threshold_correction, 'max': settings.threshold_bear, 'color': '#F59E0B', 'multiplier': settings.multiplier_correction},
        {'name': 'Bear Market', 'min': settings.threshold_bear, 'max': settings.threshold_crash, 'color': '#EF4444', 'multiplier': settings.multiplier_bear},
        {'name': 'Crash', 'min': settings.threshold_crash, 'max': 50, 'color': '#DC2626', 'multiplier': settings.multiplier_crash}
    ]
    
    # Determine current zone
    current_zone = 'Normal'
    for zone in zones:
        if zone['min'] <= drawdown < zone['max']:
            current_zone = zone['name']
            break
    if drawdown >= settings.threshold_crash:
        current_zone = 'Crash'
    
    return jsonify({
        'success': True,
        'data': {
            'current_drawdown': round(drawdown, 2),
            'current_zone': current_zone,
            'needle_position': min(drawdown / 50 * 100, 100),  # Percentage position (max 50% drawdown)
            'zones': zones,
            'index_ticker': settings.index_ticker,
            'current_price': round(market_status.get('current_price', 0), 2),
            'ath_price': round(market_status.get('ath', 0), 2)
        }
    })
