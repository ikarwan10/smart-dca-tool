"""
Market Service
==============
Market analysis and condition monitoring.
"""

from typing import Dict, Optional
from app.services.price_service import calculate_ath_and_drawdown, get_stock_price
from app.services.dca_engine import determine_market_condition, MarketCondition


# Default market index
DEFAULT_INDEX = '^GSPC'  # S&P 500


def get_market_status(index_ticker: str = DEFAULT_INDEX) -> Optional[Dict]:
    """
    Get current market status based on index drawdown.
    
    Args:
        index_ticker: Market index to analyze (default: S&P 500)
        
    Returns:
        Dictionary with market status information
        
    Example:
        >>> status = get_market_status()
        >>> print(f"Market is in {status['condition']} mode")
    """
    ath_data = calculate_ath_and_drawdown(index_ticker, period="1y")
    
    if not ath_data:
        return None
    
    condition = determine_market_condition(ath_data['drawdown_percent'])
    
    return {
        'index': index_ticker,
        'current_price': ath_data['current'],
        'ath': ath_data['ath'],
        'drawdown_percent': ath_data['drawdown_percent'],
        'condition': condition.value,
        'condition_display': condition.value.replace('_', ' ').title(),
        'is_opportunity': condition != MarketCondition.NORMAL,
        'signal': _get_signal_text(condition)
    }


def _get_signal_text(condition: MarketCondition) -> str:
    """Get human-readable signal text for market condition."""
    signals = {
        MarketCondition.NORMAL: "Standard DCA - Market near highs",
        MarketCondition.MILD_DIP: "Mild Opportunity - Consider 1.5x investment",
        MarketCondition.CORRECTION: "Correction - Good time to buy, 2x investment",
        MarketCondition.BEAR: "Bear Market - Strong buy signal, 2.5x investment",
        MarketCondition.CRASH: "Market Crash - Maximum opportunity, 3x investment"
    }
    return signals.get(condition, "Unknown condition")


def get_market_health_color(condition: str) -> str:
    """Get color code for market condition (for UI)."""
    colors = {
        'normal': '#10B981',      # Green
        'mild_dip': '#3B82F6',    # Blue
        'correction': '#F59E0B',  # Amber
        'bear': '#EF4444',        # Red
        'crash': '#DC2626'        # Dark Red
    }
    return colors.get(condition, '#6B7280')


def scan_opportunities(tickers: list, threshold: float = 10.0) -> list:
    """
    Scan multiple tickers for buying opportunities.
    
    Args:
        tickers: List of stock tickers to scan
        threshold: Minimum drawdown % to consider as opportunity
        
    Returns:
        List of stocks with opportunities, sorted by drawdown
    """
    opportunities = []
    
    for ticker in tickers:
        ath_data = calculate_ath_and_drawdown(ticker)
        if ath_data and ath_data['drawdown_percent'] >= threshold:
            condition = determine_market_condition(ath_data['drawdown_percent'])
            opportunities.append({
                'ticker': ticker,
                'drawdown_percent': ath_data['drawdown_percent'],
                'current_price': ath_data['current'],
                'ath': ath_data['ath'],
                'condition': condition.value,
                'discount': f"{ath_data['drawdown_percent']:.1f}% off ATH"
            })
    
    # Sort by drawdown (biggest opportunity first)
    return sorted(opportunities, key=lambda x: x['drawdown_percent'], reverse=True)
