"""
Settings Routes
================
User settings management.
"""

from flask import Blueprint, request, jsonify
from app.models.models import db, Settings

bp = Blueprint('settings', __name__)


def get_or_create_settings():
    """Get existing settings or create defaults."""
    settings = Settings.query.first()
    if not settings:
        settings = Settings()
        db.session.add(settings)
        db.session.commit()
    return settings


@bp.route('/settings', methods=['GET'])
def get_settings():
    """Get current settings."""
    settings = get_or_create_settings()
    return jsonify({
        'success': True,
        'data': settings.to_dict()
    })


@bp.route('/settings', methods=['PUT'])
def update_settings():
    """Update settings."""
    settings = get_or_create_settings()
    data = request.get_json()
    
    # Update base investment
    if 'base_investment' in data:
        settings.base_investment = float(data['base_investment'])
    
    # Update index ticker
    if 'index_ticker' in data:
        settings.index_ticker = data['index_ticker']
    
    # Update thresholds
    if 'threshold_mild_dip' in data:
        settings.threshold_mild_dip = float(data['threshold_mild_dip'])
    if 'threshold_correction' in data:
        settings.threshold_correction = float(data['threshold_correction'])
    if 'threshold_bear' in data:
        settings.threshold_bear = float(data['threshold_bear'])
    if 'threshold_crash' in data:
        settings.threshold_crash = float(data['threshold_crash'])
    
    # Update multipliers
    if 'multiplier_normal' in data:
        settings.multiplier_normal = float(data['multiplier_normal'])
    if 'multiplier_mild_dip' in data:
        settings.multiplier_mild_dip = float(data['multiplier_mild_dip'])
    if 'multiplier_correction' in data:
        settings.multiplier_correction = float(data['multiplier_correction'])
    if 'multiplier_bear' in data:
        settings.multiplier_bear = float(data['multiplier_bear'])
    if 'multiplier_crash' in data:
        settings.multiplier_crash = float(data['multiplier_crash'])
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Settings updated',
        'data': settings.to_dict()
    })


@bp.route('/settings/reset', methods=['POST'])
def reset_settings():
    """Reset settings to defaults."""
    settings = get_or_create_settings()
    
    # Reset to defaults
    settings.base_investment = 500.0
    settings.index_ticker = '^GSPC'
    settings.threshold_mild_dip = 5.0
    settings.threshold_correction = 10.0
    settings.threshold_bear = 20.0
    settings.threshold_crash = 30.0
    settings.multiplier_normal = 1.0
    settings.multiplier_mild_dip = 1.5
    settings.multiplier_correction = 2.0
    settings.multiplier_bear = 2.5
    settings.multiplier_crash = 3.0
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Settings reset to defaults',
        'data': settings.to_dict()
    })
