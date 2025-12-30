"""
Database Models
===============
SQLAlchemy models for the Smart DCA Investment Tool.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# This will be initialized by the main app
db = SQLAlchemy()


class Portfolio(db.Model):
    """User portfolio containing multiple holdings."""
    __tablename__ = 'portfolios'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default='My Portfolio')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    holdings = db.relationship('Holding', backref='portfolio', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'holdings': [h.to_dict() for h in self.holdings]
        }


class Holding(db.Model):
    """Individual stock holding within a portfolio."""
    __tablename__ = 'holdings'
    
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100))
    target_allocation = db.Column(db.Float, default=0.0)  # Percentage (0-100)
    shares_owned = db.Column(db.Float, default=0.0)
    cost_basis = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'ticker': self.ticker,
            'name': self.name,
            'target_allocation': self.target_allocation,
            'shares_owned': self.shares_owned,
            'cost_basis': self.cost_basis
        }


class Settings(db.Model):
    """User settings for DCA calculations."""
    __tablename__ = 'settings'
    
    id = db.Column(db.Integer, primary_key=True)
    base_investment = db.Column(db.Float, default=500.0)
    index_ticker = db.Column(db.String(10), default='^GSPC')  # S&P 500
    
    # Multiplier thresholds (% below ATH)
    threshold_mild_dip = db.Column(db.Float, default=5.0)
    threshold_correction = db.Column(db.Float, default=10.0)
    threshold_bear = db.Column(db.Float, default=20.0)
    threshold_crash = db.Column(db.Float, default=30.0)
    
    # Multiplier values
    multiplier_normal = db.Column(db.Float, default=1.0)
    multiplier_mild_dip = db.Column(db.Float, default=1.5)
    multiplier_correction = db.Column(db.Float, default=2.0)
    multiplier_bear = db.Column(db.Float, default=2.5)
    multiplier_crash = db.Column(db.Float, default=3.0)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'base_investment': self.base_investment,
            'index_ticker': self.index_ticker,
            'thresholds': {
                'mild_dip': self.threshold_mild_dip,
                'correction': self.threshold_correction,
                'bear': self.threshold_bear,
                'crash': self.threshold_crash
            },
            'multipliers': {
                'normal': self.multiplier_normal,
                'mild_dip': self.multiplier_mild_dip,
                'correction': self.multiplier_correction,
                'bear': self.multiplier_bear,
                'crash': self.multiplier_crash
            }
        }


class InvestmentLog(db.Model):
    """Log of investments made following DCA recommendations."""
    __tablename__ = 'investment_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    shares = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    market_condition = db.Column(db.String(20))
    multiplier_used = db.Column(db.Float)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'ticker': self.ticker,
            'shares': self.shares,
            'price': self.price,
            'total_amount': self.total_amount,
            'market_condition': self.market_condition,
            'multiplier_used': self.multiplier_used,
            'notes': self.notes
        }
