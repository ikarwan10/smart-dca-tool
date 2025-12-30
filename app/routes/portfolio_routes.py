"""
Portfolio Routes
================
CRUD operations for portfolio and holdings management.
"""

from flask import Blueprint, request, jsonify
from app.models.models import db, Portfolio, Holding
from app.services import price_service

bp = Blueprint('portfolio', __name__)


# ============================================
# Portfolio Endpoints
# ============================================

@bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    """Get the user's portfolio with all holdings."""
    # Get or create default portfolio
    portfolio = Portfolio.query.first()
    if not portfolio:
        portfolio = Portfolio(name='My Portfolio')
        db.session.add(portfolio)
        db.session.commit()
    
    # Get current prices for all holdings
    holdings_data = []
    total_value = 0
    
    for holding in portfolio.holdings:
        price = price_service.get_stock_price(holding.ticker)
        current_value = (holding.shares_owned or 0) * (price or 0)
        total_value += current_value
        
        holdings_data.append({
            'id': holding.id,
            'ticker': holding.ticker,
            'name': holding.name,
            'target_allocation': holding.target_allocation,
            'shares_owned': holding.shares_owned,
            'cost_basis': holding.cost_basis,
            'current_price': price,
            'current_value': round(current_value, 2)
        })
    
    # Calculate actual allocations
    for h in holdings_data:
        h['actual_allocation'] = round((h['current_value'] / total_value * 100) if total_value > 0 else 0, 1)
    
    return jsonify({
        'success': True,
        'data': {
            'id': portfolio.id,
            'name': portfolio.name,
            'holdings': holdings_data,
            'total_value': round(total_value, 2),
            'holdings_count': len(holdings_data)
        }
    })


@bp.route('/holdings', methods=['POST'])
def add_holding():
    """Add a new holding to the portfolio."""
    data = request.get_json()
    
    # Validate required fields
    ticker = data.get('ticker', '').upper().strip()
    if not ticker:
        return jsonify({'success': False, 'error': 'Ticker is required'}), 400
    
    # Validate ticker exists
    if not price_service.validate_ticker(ticker):
        return jsonify({'success': False, 'error': f'Invalid ticker: {ticker}'}), 400
    
    # Get or create portfolio
    portfolio = Portfolio.query.first()
    if not portfolio:
        portfolio = Portfolio(name='My Portfolio')
        db.session.add(portfolio)
        db.session.commit()
    
    # Check if holding already exists
    existing = Holding.query.filter_by(portfolio_id=portfolio.id, ticker=ticker).first()
    if existing:
        return jsonify({'success': False, 'error': f'{ticker} already in portfolio'}), 400
    
    # Get stock info for name
    stock_info = price_service.get_stock_info(ticker)
    name = data.get('name') or (stock_info.get('name') if stock_info else ticker)
    
    # Create holding
    holding = Holding(
        portfolio_id=portfolio.id,
        ticker=ticker,
        name=name,
        target_allocation=float(data.get('target_allocation', 0)),
        shares_owned=float(data.get('shares_owned', 0)),
        cost_basis=float(data.get('cost_basis', 0))
    )
    
    db.session.add(holding)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'{ticker} added to portfolio',
        'data': holding.to_dict()
    })


@bp.route('/holdings/<int:holding_id>', methods=['GET'])
def get_holding(holding_id):
    """Get a specific holding."""
    holding = Holding.query.get_or_404(holding_id)
    price = price_service.get_stock_price(holding.ticker)
    
    data = holding.to_dict()
    data['current_price'] = price
    data['current_value'] = round((holding.shares_owned or 0) * (price or 0), 2)
    
    return jsonify({'success': True, 'data': data})


@bp.route('/holdings/<int:holding_id>', methods=['PUT'])
def update_holding(holding_id):
    """Update a holding."""
    holding = Holding.query.get_or_404(holding_id)
    data = request.get_json()
    
    # Update fields if provided
    if 'name' in data:
        holding.name = data['name']
    if 'target_allocation' in data:
        holding.target_allocation = float(data['target_allocation'])
    if 'shares_owned' in data:
        holding.shares_owned = float(data['shares_owned'])
    if 'cost_basis' in data:
        holding.cost_basis = float(data['cost_basis'])
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'{holding.ticker} updated',
        'data': holding.to_dict()
    })


@bp.route('/holdings/<int:holding_id>', methods=['DELETE'])
def delete_holding(holding_id):
    """Delete a holding."""
    holding = Holding.query.get_or_404(holding_id)
    ticker = holding.ticker
    
    db.session.delete(holding)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'{ticker} removed from portfolio'
    })


@bp.route('/holdings/reorder', methods=['POST'])
def reorder_holdings():
    """Update target allocations for multiple holdings at once."""
    data = request.get_json()
    allocations = data.get('allocations', [])
    
    for item in allocations:
        holding = Holding.query.get(item.get('id'))
        if holding:
            holding.target_allocation = float(item.get('target_allocation', 0))
    
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Allocations updated'})
