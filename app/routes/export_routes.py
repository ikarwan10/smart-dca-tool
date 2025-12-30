"""
Export Routes
=============
Routes for exporting data to CSV and other formats.
"""

from flask import Blueprint, Response, request, jsonify
from datetime import datetime
import csv
import io
from app.models.models import db, Portfolio, Holding, InvestmentLog, Settings
from app.services import price_service

bp = Blueprint('export', __name__)


@bp.route('/export/portfolio', methods=['GET'])
def export_portfolio():
    """Export portfolio holdings to CSV."""
    portfolio = Portfolio.query.first()
    if not portfolio or not portfolio.holdings:
        return jsonify({'success': False, 'error': 'No portfolio data to export'}), 404
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header row
    writer.writerow([
        'Ticker', 'Name', 'Target Allocation (%)', 'Shares Owned', 
        'Cost Basis ($)', 'Current Price ($)', 'Current Value ($)',
        'Gain/Loss ($)', 'Gain/Loss (%)'
    ])
    
    # Data rows
    for holding in portfolio.holdings:
        current_price = price_service.get_stock_price(holding.ticker) or 0
        current_value = (holding.shares_owned or 0) * current_price
        cost_basis = holding.cost_basis or 0
        gain_loss = current_value - cost_basis
        gain_loss_pct = (gain_loss / cost_basis * 100) if cost_basis > 0 else 0
        
        writer.writerow([
            holding.ticker,
            holding.name or '',
            holding.target_allocation or 0,
            holding.shares_owned or 0,
            round(cost_basis, 2),
            round(current_price, 2),
            round(current_value, 2),
            round(gain_loss, 2),
            round(gain_loss_pct, 2)
        ])
    
    # Prepare response
    output.seek(0)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'portfolio_export_{timestamp}.csv'
    
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )


@bp.route('/export/investments', methods=['GET'])
def export_investments():
    """Export investment history to CSV."""
    # Get filter parameters
    ticker = request.args.get('ticker')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    query = InvestmentLog.query
    
    if ticker:
        query = query.filter(InvestmentLog.ticker == ticker.upper())
    if start_date:
        try:
            from datetime import datetime as dt
            start = dt.strptime(start_date, '%Y-%m-%d').date()
            query = query.filter(InvestmentLog.date >= start)
        except ValueError:
            pass
    if end_date:
        try:
            from datetime import datetime as dt
            end = dt.strptime(end_date, '%Y-%m-%d').date()
            query = query.filter(InvestmentLog.date <= end)
        except ValueError:
            pass
    
    investments = query.order_by(InvestmentLog.date.desc()).all()
    
    if not investments:
        return jsonify({'success': False, 'error': 'No investment data to export'}), 404
    
    # Create CSV
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow([
        'Date', 'Ticker', 'Shares', 'Price ($)', 'Total Amount ($)',
        'Market Condition', 'Multiplier', 'Notes'
    ])
    
    # Data
    for inv in investments:
        writer.writerow([
            inv.date.strftime('%Y-%m-%d'),
            inv.ticker,
            inv.shares,
            round(inv.price, 2),
            round(inv.total_amount, 2),
            inv.market_condition or '',
            inv.multiplier_used or '',
            inv.notes or ''
        ])
    
    # Totals row
    total_invested = sum(inv.total_amount for inv in investments)
    writer.writerow([])
    writer.writerow(['TOTAL', '', '', '', round(total_invested, 2), '', '', ''])
    
    output.seek(0)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'investment_history_{timestamp}.csv'
    
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )


@bp.route('/export/dca-plan', methods=['GET'])
def export_dca_plan():
    """Export current DCA recommendation to CSV."""
    from app.services import dca_engine, market_service
    
    # Get settings
    settings = Settings.query.first()
    if not settings:
        return jsonify({'success': False, 'error': 'No settings configured'}), 404
    
    # Get portfolio
    portfolio = Portfolio.query.first()
    if not portfolio or not portfolio.holdings:
        return jsonify({'success': False, 'error': 'No portfolio configured'}), 404
    
    # Get market data
    market_status = market_service.get_market_status(settings.index_ticker)
    if not market_status:
        return jsonify({'success': False, 'error': 'Could not fetch market data'}), 500
    
    # Calculate DCA
    holdings_data = []
    prices = {}
    for h in portfolio.holdings:
        price = price_service.get_stock_price(h.ticker)
        if price:
            prices[h.ticker] = price
            holdings_data.append({
                'ticker': h.ticker,
                'name': h.name,
                'target_allocation': h.target_allocation
            })
    
    if not holdings_data:
        return jsonify({'success': False, 'error': 'Could not fetch stock prices'}), 500
    
    # Get multipliers from settings
    multipliers = {
        'normal': settings.multiplier_normal,
        'mild_dip': settings.multiplier_mild_dip,
        'correction': settings.multiplier_correction,
        'bear': settings.multiplier_bear,
        'crash': settings.multiplier_crash
    }
    
    thresholds = {
        'mild_dip': settings.threshold_mild_dip,
        'correction': settings.threshold_correction,
        'bear': settings.threshold_bear,
        'crash': settings.threshold_crash
    }
    
    dca_result = dca_engine.calculate_dca(
        holdings_data, 
        prices, 
        market_status['drawdown_percent'],
        settings.base_investment,
        thresholds,
        multipliers
    )
    
    # Create CSV
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Market info header
    writer.writerow(['DCA Investment Plan'])
    writer.writerow(['Generated:', datetime.now().strftime('%Y-%m-%d %H:%M')])
    writer.writerow([])
    writer.writerow(['Market Conditions'])
    writer.writerow(['Index:', settings.index_ticker])
    writer.writerow(['Condition:', market_status['condition_display']])
    writer.writerow(['Drawdown:', f"{market_status['drawdown_percent']:.1f}%"])
    writer.writerow(['Multiplier:', f"{dca_result['multiplier']}x"])
    writer.writerow([])
    writer.writerow(['Investment Summary'])
    writer.writerow(['Base Amount:', f"${settings.base_investment}"])
    writer.writerow(['Total to Invest:', f"${dca_result['total_amount']}"])
    writer.writerow([])
    
    # Recommendations table
    writer.writerow(['Ticker', 'Name', 'Allocation (%)', 'Amount ($)', 'Current Price ($)', 'Shares to Buy'])
    
    for rec in dca_result['recommendations']:
        writer.writerow([
            rec['ticker'],
            rec.get('name', ''),
            rec['target_allocation'],
            round(rec['recommended_amount'], 2),
            round(rec['current_price'], 2),
            round(rec['recommended_shares'], 4)
        ])
    
    output.seek(0)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'dca_plan_{timestamp}.csv'
    
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )
