"""
API Routes
==========
REST API endpoints for the Smart DCA Tool.
Designed for easy migration to Wix HTTP Functions.
"""

from flask import Blueprint, jsonify, request
from app.services import price_service, dca_engine, market_service

bp = Blueprint('api', __name__)


# ============================================
# Market Endpoints
# ============================================

@bp.route('/market/status')
def get_market_status():
    """
    Get current market status and condition.
    
    Returns:
        JSON with market status
        
    Wix Migration: This becomes an HTTP Function
    """
    index = request.args.get('index', '^GSPC')
    status = market_service.get_market_status(index)
    
    if status:
        return jsonify({'success': True, 'data': status})
    return jsonify({'success': False, 'error': 'Could not fetch market data'}), 500


@bp.route('/market/opportunities')
def get_opportunities():
    """
    Scan for buying opportunities across common ETFs.
    """
    # Default ETFs to scan
    tickers = ['VOO', 'QQQ', 'VTI', 'SCHD', 'VGT', 'VUG', 'VTV']
    threshold = float(request.args.get('threshold', 10))
    
    opportunities = market_service.scan_opportunities(tickers, threshold)
    return jsonify({'success': True, 'data': opportunities})


# ============================================
# Price Endpoints
# ============================================

@bp.route('/price/<ticker>')
def get_price(ticker):
    """
    Get current price for a ticker.
    
    Args:
        ticker: Stock symbol
    """
    price = price_service.get_stock_price(ticker.upper())
    
    if price:
        return jsonify({'success': True, 'ticker': ticker.upper(), 'price': price})
    return jsonify({'success': False, 'error': f'Could not fetch price for {ticker}'}), 404


@bp.route('/price/batch', methods=['POST'])
def get_batch_prices():
    """
    Get prices for multiple tickers.
    
    Request body:
        {"tickers": ["AAPL", "MSFT", "GOOGL"]}
    """
    data = request.get_json()
    tickers = data.get('tickers', [])
    
    if not tickers:
        return jsonify({'success': False, 'error': 'No tickers provided'}), 400
    
    prices = price_service.get_batch_prices(tickers)
    return jsonify({'success': True, 'data': prices})


@bp.route('/stock/<ticker>/info')
def get_stock_info(ticker):
    """Get detailed stock information."""
    info = price_service.get_stock_info(ticker.upper())
    
    if info:
        return jsonify({'success': True, 'data': info})
    return jsonify({'success': False, 'error': f'Could not fetch info for {ticker}'}), 404


@bp.route('/stock/<ticker>/ath')
def get_ath_info(ticker):
    """Get ATH and drawdown information."""
    period = request.args.get('period', '1y')
    ath_data = price_service.calculate_ath_and_drawdown(ticker.upper(), period)
    
    if ath_data:
        return jsonify({'success': True, 'data': ath_data})
    return jsonify({'success': False, 'error': f'Could not fetch ATH data for {ticker}'}), 404


# ============================================
# DCA Calculation Endpoints
# ============================================

@bp.route('/dca/calculate', methods=['POST'])
def calculate_dca():
    """
    Calculate DCA recommendation.
    
    Request body:
        {
            "holdings": [
                {"ticker": "VOO", "name": "S&P 500 ETF", "target_allocation": 60},
                {"ticker": "QQQ", "name": "Nasdaq ETF", "target_allocation": 40}
            ],
            "base_amount": 500,
            "index_ticker": "^GSPC"  // optional
        }
        
    Returns:
        Complete DCA recommendation
        
    Wix Migration: This is the main calculation endpoint
    """
    data = request.get_json()
    
    # Validate request
    holdings = data.get('holdings', [])
    base_amount = float(data.get('base_amount', 500))
    index_ticker = data.get('index_ticker', '^GSPC')
    
    if not holdings:
        return jsonify({'success': False, 'error': 'No holdings provided'}), 400
    
    # Get market status
    market_status = market_service.get_market_status(index_ticker)
    if not market_status:
        return jsonify({'success': False, 'error': 'Could not fetch market data'}), 500
    
    # Get current prices for all holdings
    tickers = [h['ticker'] for h in holdings]
    prices = price_service.get_batch_prices(tickers)
    
    # Check for missing prices
    missing = [t for t, p in prices.items() if p is None]
    if missing:
        return jsonify({
            'success': False, 
            'error': f'Could not fetch prices for: {", ".join(missing)}'
        }), 404
    
    # Calculate DCA
    result = dca_engine.calculate_dca(
        holdings=holdings,
        current_prices=prices,
        market_drawdown=market_status['drawdown_percent'],
        base_amount=base_amount
    )
    
    return jsonify({'success': True, 'data': result})


@bp.route('/dca/multiplier')
def get_multiplier():
    """
    Get current investment multiplier based on market conditions.
    Quick endpoint for dashboard display.
    """
    index = request.args.get('index', '^GSPC')
    base = float(request.args.get('base', 500))
    
    market_status = market_service.get_market_status(index)
    if not market_status:
        return jsonify({'success': False, 'error': 'Could not fetch market data'}), 500
    
    result = dca_engine.calculate_investment_amount(
        base_amount=base,
        drawdown_percent=market_status['drawdown_percent']
    )
    
    return jsonify({'success': True, 'data': result})


# ============================================
# Utility Endpoints
# ============================================

@bp.route('/validate/<ticker>')
def validate_ticker(ticker):
    """Check if a ticker symbol is valid."""
    is_valid = price_service.validate_ticker(ticker.upper())
    return jsonify({'success': True, 'ticker': ticker.upper(), 'valid': is_valid})
