"""
Investment Routes
=================
Routes for logging and viewing investment history.
"""

from flask import Blueprint, request, jsonify
from datetime import datetime, date
from app.models.models import db, InvestmentLog, Holding, Portfolio
from app.services import price_service

bp = Blueprint('investments', __name__)


# ============================================
# Investment Log Endpoints
# ============================================

@bp.route('/investments', methods=['GET'])
def get_investments():
    """Get all investment logs with optional filtering."""
    # Query parameters for filtering
    ticker = request.args.get('ticker')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    limit = request.args.get('limit', type=int)
    
    query = InvestmentLog.query
    
    # Apply filters
    if ticker:
        query = query.filter(InvestmentLog.ticker == ticker.upper())
    
    if start_date:
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d').date()
            query = query.filter(InvestmentLog.date >= start)
        except ValueError:
            pass
    
    if end_date:
        try:
            end = datetime.strptime(end_date, '%Y-%m-%d').date()
            query = query.filter(InvestmentLog.date <= end)
        except ValueError:
            pass
    
    # Order by date descending (newest first)
    query = query.order_by(InvestmentLog.date.desc(), InvestmentLog.created_at.desc())
    
    if limit:
        query = query.limit(limit)
    
    investments = query.all()
    
    # Calculate summary stats
    total_invested = sum(inv.total_amount for inv in investments)
    total_shares = {}
    for inv in investments:
        total_shares[inv.ticker] = total_shares.get(inv.ticker, 0) + inv.shares
    
    return jsonify({
        'success': True,
        'data': {
            'investments': [inv.to_dict() for inv in investments],
            'count': len(investments),
            'total_invested': round(total_invested, 2),
            'shares_by_ticker': total_shares
        }
    })


@bp.route('/investments', methods=['POST'])
def log_investment():
    """Log a new investment."""
    data = request.get_json()
    
    # Validate required fields
    ticker = data.get('ticker', '').upper().strip()
    if not ticker:
        return jsonify({'success': False, 'error': 'Ticker is required'}), 400
    
    shares = data.get('shares')
    if shares is None or shares <= 0:
        return jsonify({'success': False, 'error': 'Shares must be a positive number'}), 400
    
    price = data.get('price')
    if price is None or price <= 0:
        return jsonify({'success': False, 'error': 'Price must be a positive number'}), 400
    
    # Parse date (default to today)
    date_str = data.get('date')
    if date_str:
        try:
            inv_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'success': False, 'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    else:
        inv_date = date.today()
    
    # Calculate total
    total_amount = round(shares * price, 2)
    
    # Create investment log
    investment = InvestmentLog(
        date=inv_date,
        ticker=ticker,
        shares=float(shares),
        price=float(price),
        total_amount=total_amount,
        market_condition=data.get('market_condition'),
        multiplier_used=data.get('multiplier_used'),
        notes=data.get('notes')
    )
    
    db.session.add(investment)
    
    # Optionally update the holding's shares_owned and cost_basis
    if data.get('update_holding', True):
        portfolio = Portfolio.query.first()
        if portfolio:
            holding = Holding.query.filter_by(
                portfolio_id=portfolio.id, 
                ticker=ticker
            ).first()
            
            if holding:
                # Update shares and cost basis
                old_shares = holding.shares_owned or 0
                old_cost = holding.cost_basis or 0
                new_total_shares = old_shares + shares
                new_total_cost = old_cost + total_amount
                
                holding.shares_owned = new_total_shares
                holding.cost_basis = new_total_cost
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'Investment logged: {shares} shares of {ticker} at ${price}',
        'data': investment.to_dict()
    }), 201


@bp.route('/investments/<int:investment_id>', methods=['GET'])
def get_investment(investment_id):
    """Get a specific investment log."""
    investment = InvestmentLog.query.get_or_404(investment_id)
    return jsonify({
        'success': True,
        'data': investment.to_dict()
    })


@bp.route('/investments/<int:investment_id>', methods=['PUT'])
def update_investment(investment_id):
    """Update an investment log."""
    investment = InvestmentLog.query.get_or_404(investment_id)
    data = request.get_json()
    
    # Update fields if provided
    if 'shares' in data:
        if data['shares'] <= 0:
            return jsonify({'success': False, 'error': 'Shares must be positive'}), 400
        investment.shares = float(data['shares'])
    
    if 'price' in data:
        if data['price'] <= 0:
            return jsonify({'success': False, 'error': 'Price must be positive'}), 400
        investment.price = float(data['price'])
    
    if 'date' in data:
        try:
            investment.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'success': False, 'error': 'Invalid date format'}), 400
    
    if 'notes' in data:
        investment.notes = data['notes']
    
    # Recalculate total
    investment.total_amount = round(investment.shares * investment.price, 2)
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Investment updated',
        'data': investment.to_dict()
    })


@bp.route('/investments/<int:investment_id>', methods=['DELETE'])
def delete_investment(investment_id):
    """Delete an investment log."""
    investment = InvestmentLog.query.get_or_404(investment_id)
    
    db.session.delete(investment)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': f'Investment {investment_id} deleted'
    })


# ============================================
# Performance Calculation Endpoints
# ============================================

@bp.route('/investments/summary', methods=['GET'])
def get_investment_summary():
    """Get investment summary and performance metrics."""
    investments = InvestmentLog.query.order_by(InvestmentLog.date.asc()).all()
    
    if not investments:
        return jsonify({
            'success': True,
            'data': {
                'total_invested': 0,
                'total_value': 0,
                'total_gain': 0,
                'total_gain_percent': 0,
                'by_ticker': {},
                'by_month': [],
                'investment_count': 0
            }
        })
    
    # Calculate per-ticker performance
    ticker_data = {}
    for inv in investments:
        if inv.ticker not in ticker_data:
            ticker_data[inv.ticker] = {
                'ticker': inv.ticker,
                'total_shares': 0,
                'total_invested': 0,
                'avg_cost': 0,
                'investments': []
            }
        
        ticker_data[inv.ticker]['total_shares'] += inv.shares
        ticker_data[inv.ticker]['total_invested'] += inv.total_amount
        ticker_data[inv.ticker]['investments'].append({
            'date': inv.date.isoformat(),
            'shares': inv.shares,
            'price': inv.price,
            'amount': inv.total_amount
        })
    
    # Calculate average cost and current value for each ticker
    total_invested = 0
    total_current_value = 0
    
    for ticker, data in ticker_data.items():
        total_invested += data['total_invested']
        
        if data['total_shares'] > 0:
            data['avg_cost'] = round(data['total_invested'] / data['total_shares'], 2)
        
        # Get current price
        current_price = price_service.get_stock_price(ticker)
        if current_price:
            data['current_price'] = current_price
            data['current_value'] = round(data['total_shares'] * current_price, 2)
            data['gain'] = round(data['current_value'] - data['total_invested'], 2)
            data['gain_percent'] = round((data['gain'] / data['total_invested']) * 100, 2) if data['total_invested'] > 0 else 0
            total_current_value += data['current_value']
        else:
            data['current_price'] = None
            data['current_value'] = None
            data['gain'] = None
            data['gain_percent'] = None
    
    # Calculate monthly summary
    monthly_data = {}
    for inv in investments:
        month_key = inv.date.strftime('%Y-%m')
        if month_key not in monthly_data:
            monthly_data[month_key] = {
                'month': month_key,
                'invested': 0,
                'investments': 0
            }
        monthly_data[month_key]['invested'] += inv.total_amount
        monthly_data[month_key]['investments'] += 1
    
    monthly_summary = sorted(monthly_data.values(), key=lambda x: x['month'])
    
    # Running total for chart
    running_total = 0
    for month in monthly_summary:
        running_total += month['invested']
        month['cumulative'] = round(running_total, 2)
    
    total_gain = total_current_value - total_invested if total_current_value > 0 else 0
    total_gain_percent = (total_gain / total_invested * 100) if total_invested > 0 else 0
    
    return jsonify({
        'success': True,
        'data': {
            'total_invested': round(total_invested, 2),
            'total_value': round(total_current_value, 2) if total_current_value > 0 else None,
            'total_gain': round(total_gain, 2) if total_current_value > 0 else None,
            'total_gain_percent': round(total_gain_percent, 2) if total_current_value > 0 else None,
            'by_ticker': ticker_data,
            'by_month': monthly_summary,
            'investment_count': len(investments)
        }
    })


@bp.route('/investments/chart-data', methods=['GET'])
def get_chart_data():
    """Get data formatted for performance charts."""
    investments = InvestmentLog.query.order_by(InvestmentLog.date.asc()).all()
    
    if not investments:
        return jsonify({
            'success': True,
            'data': {
                'labels': [],
                'invested': [],
                'cumulative': []
            }
        })
    
    # Group by month
    monthly_data = {}
    for inv in investments:
        month_key = inv.date.strftime('%b %Y')
        if month_key not in monthly_data:
            monthly_data[month_key] = 0
        monthly_data[month_key] += inv.total_amount
    
    labels = list(monthly_data.keys())
    invested = list(monthly_data.values())
    
    # Calculate cumulative
    cumulative = []
    running_total = 0
    for amount in invested:
        running_total += amount
        cumulative.append(round(running_total, 2))
    
    return jsonify({
        'success': True,
        'data': {
            'labels': labels,
            'invested': [round(x, 2) for x in invested],
            'cumulative': cumulative
        }
    })
