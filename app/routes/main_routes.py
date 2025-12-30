"""
Main Routes
===========
Web page routes for the Smart DCA Tool.
"""

from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def dashboard():
    """Dashboard / Home page."""
    return render_template('dashboard.html')


@bp.route('/planner')
def planner():
    """DCA Planner page."""
    return render_template('planner.html')


@bp.route('/portfolio')
def portfolio():
    """Portfolio management page."""
    return render_template('portfolio.html')


@bp.route('/market')
def market():
    """Market analysis page."""
    return render_template('market.html')


@bp.route('/history')
def history():
    """Investment history page."""
    return render_template('history.html')


@bp.route('/settings')
def settings():
    """Settings page."""
    return render_template('settings.html')
