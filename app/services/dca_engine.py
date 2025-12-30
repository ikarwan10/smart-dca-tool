"""
DCA Calculation Engine
======================
Core business logic for Dollar Cost Averaging calculations.
Based on Tom Lee's DCA Strategy principles.

This module is designed to be pure Python with no Flask dependencies,
making it easy to migrate to Wix/JavaScript later.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class MarketCondition(Enum):
    """Market conditions based on drawdown from ATH."""
    NORMAL = "normal"           # At or near ATH (0-5% below)
    MILD_DIP = "mild_dip"       # 5-10% below ATH
    CORRECTION = "correction"   # 10-20% below ATH
    BEAR = "bear"               # 20-30% below ATH
    CRASH = "crash"             # 30%+ below ATH


@dataclass
class DCARecommendation:
    """Recommendation for a single stock."""
    ticker: str
    name: str
    current_price: float
    target_allocation: float
    recommended_amount: float
    recommended_shares: float
    allocation_after: float


@dataclass  
class DCAResult:
    """Complete DCA calculation result."""
    market_condition: MarketCondition
    drawdown_percent: float
    multiplier: float
    base_amount: float
    total_investment: float
    recommendations: List[DCARecommendation]
    timestamp: str


# Default thresholds (% below ATH)
DEFAULT_THRESHOLDS = {
    'mild_dip': 5.0,
    'correction': 10.0,
    'bear': 20.0,
    'crash': 30.0
}

# Default multipliers
DEFAULT_MULTIPLIERS = {
    'normal': 1.0,
    'mild_dip': 1.5,
    'correction': 2.0,
    'bear': 2.5,
    'crash': 3.0
}


def determine_market_condition(
    drawdown_percent: float,
    thresholds: Dict[str, float] = None
) -> MarketCondition:
    """
    Determine market condition based on drawdown percentage.
    
    Args:
        drawdown_percent: How far below ATH (0 = at ATH, 10 = 10% below)
        thresholds: Custom thresholds (optional)
        
    Returns:
        MarketCondition enum value
        
    Example:
        >>> condition = determine_market_condition(15.0)
        >>> print(condition)  # MarketCondition.CORRECTION
    """
    t = thresholds or DEFAULT_THRESHOLDS
    
    if drawdown_percent >= t['crash']:
        return MarketCondition.CRASH
    elif drawdown_percent >= t['bear']:
        return MarketCondition.BEAR
    elif drawdown_percent >= t['correction']:
        return MarketCondition.CORRECTION
    elif drawdown_percent >= t['mild_dip']:
        return MarketCondition.MILD_DIP
    else:
        return MarketCondition.NORMAL


def get_multiplier(
    condition: MarketCondition,
    multipliers: Dict[str, float] = None
) -> float:
    """
    Get investment multiplier for a market condition.
    
    Args:
        condition: Current market condition
        multipliers: Custom multiplier values (optional)
        
    Returns:
        Multiplier value (1.0 to 3.0 typically)
        
    Example:
        >>> mult = get_multiplier(MarketCondition.CORRECTION)
        >>> print(mult)  # 2.0
    """
    m = multipliers or DEFAULT_MULTIPLIERS
    return m.get(condition.value, 1.0)


def calculate_investment_amount(
    base_amount: float,
    drawdown_percent: float,
    thresholds: Dict[str, float] = None,
    multipliers: Dict[str, float] = None
) -> Dict:
    """
    Calculate total investment amount based on market conditions.
    
    This is the core of Tom Lee's strategy: invest more when markets
    are down (buying the dip at a discount).
    
    Args:
        base_amount: Normal monthly investment
        drawdown_percent: Current drawdown from ATH
        thresholds: Custom thresholds
        multipliers: Custom multipliers
        
    Returns:
        Dictionary with condition, multiplier, and total amount
        
    Example:
        >>> result = calculate_investment_amount(500, 25.0)
        >>> print(f"Invest ${result['total_amount']} (Bear market, 2.5x)")
    """
    condition = determine_market_condition(drawdown_percent, thresholds)
    multiplier = get_multiplier(condition, multipliers)
    total = base_amount * multiplier
    
    return {
        'condition': condition.value,
        'condition_display': condition.value.replace('_', ' ').title(),
        'drawdown_percent': round(drawdown_percent, 2),
        'multiplier': multiplier,
        'base_amount': base_amount,
        'total_amount': round(total, 2)
    }


def calculate_allocation(
    holdings: List[Dict],
    total_investment: float,
    current_prices: Dict[str, float]
) -> List[Dict]:
    """
    Calculate how to allocate investment across holdings.
    
    Args:
        holdings: List of holdings with target_allocation percentages
        total_investment: Total amount to invest
        current_prices: Dict mapping ticker to current price
        
    Returns:
        List of allocation recommendations
        
    Example:
        >>> holdings = [
        ...     {'ticker': 'VOO', 'target_allocation': 60},
        ...     {'ticker': 'QQQ', 'target_allocation': 40}
        ... ]
        >>> prices = {'VOO': 450.0, 'QQQ': 380.0}
        >>> allocations = calculate_allocation(holdings, 1000, prices)
    """
    recommendations = []
    
    # Normalize allocations to 100%
    total_allocation = sum(h.get('target_allocation', 0) for h in holdings)
    
    for holding in holdings:
        ticker = holding.get('ticker')
        target_pct = holding.get('target_allocation', 0)
        name = holding.get('name', ticker)
        
        # Normalize to 100% if needed
        if total_allocation > 0:
            normalized_pct = (target_pct / total_allocation) * 100
        else:
            normalized_pct = 100 / len(holdings) if holdings else 0
        
        # Calculate amount to invest in this stock
        amount = (normalized_pct / 100) * total_investment
        
        # Calculate shares to buy
        price = current_prices.get(ticker, 0)
        shares = amount / price if price > 0 else 0
        
        recommendations.append({
            'ticker': ticker,
            'name': name,
            'current_price': round(price, 2),
            'target_allocation': round(normalized_pct, 1),
            'recommended_amount': round(amount, 2),
            'recommended_shares': round(shares, 4),
            'shares_whole': int(shares),
            'shares_fractional': round(shares, 2)
        })
    
    return recommendations


def calculate_dca(
    holdings: List[Dict],
    current_prices: Dict[str, float],
    market_drawdown: float,
    base_amount: float,
    thresholds: Dict[str, float] = None,
    multipliers: Dict[str, float] = None
) -> Dict:
    """
    Complete DCA calculation - the main entry point.
    
    This function combines all the logic to provide a complete
    DCA recommendation based on portfolio and market conditions.
    
    Args:
        holdings: List of portfolio holdings
        current_prices: Current prices for all tickers
        market_drawdown: Market index drawdown percentage
        base_amount: Base monthly investment
        thresholds: Custom thresholds (optional)
        multipliers: Custom multipliers (optional)
        
    Returns:
        Complete DCA recommendation dictionary
        
    Example:
        >>> holdings = [
        ...     {'ticker': 'VOO', 'name': 'S&P 500 ETF', 'target_allocation': 60},
        ...     {'ticker': 'QQQ', 'name': 'Nasdaq ETF', 'target_allocation': 40}
        ... ]
        >>> prices = {'VOO': 450.0, 'QQQ': 380.0}
        >>> result = calculate_dca(holdings, prices, 12.5, 500)
        >>> print(f"Market: {result['market']['condition_display']}")
        >>> print(f"Total to invest: ${result['market']['total_amount']}")
    """
    from datetime import datetime
    
    # Calculate market-adjusted investment
    market_info = calculate_investment_amount(
        base_amount, 
        market_drawdown,
        thresholds,
        multipliers
    )
    
    # Calculate per-stock allocations
    allocations = calculate_allocation(
        holdings,
        market_info['total_amount'],
        current_prices
    )
    
    return {
        'market': market_info,
        'allocations': allocations,
        'summary': {
            'total_investment': market_info['total_amount'],
            'stock_count': len(allocations),
            'timestamp': datetime.now().isoformat()
        }
    }


def format_recommendation_text(result: Dict) -> str:
    """
    Format DCA result as human-readable text.
    Useful for console output or notifications.
    
    Args:
        result: Output from calculate_dca()
        
    Returns:
        Formatted text summary
    """
    market = result['market']
    lines = [
        "=" * 50,
        "SMART DCA RECOMMENDATION",
        "=" * 50,
        f"Market Condition: {market['condition_display']}",
        f"Market Drawdown: {market['drawdown_percent']}% below ATH",
        f"Investment Multiplier: {market['multiplier']}x",
        "",
        f"Base Amount: ${market['base_amount']:.2f}",
        f"Total to Invest: ${market['total_amount']:.2f}",
        "",
        "-" * 50,
        "ALLOCATION BREAKDOWN:",
        "-" * 50,
    ]
    
    for alloc in result['allocations']:
        lines.append(
            f"  {alloc['ticker']:6} | ${alloc['recommended_amount']:>8.2f} | "
            f"{alloc['shares_whole']} shares @ ${alloc['current_price']:.2f}"
        )
    
    lines.extend([
        "-" * 50,
        f"Generated: {result['summary']['timestamp'][:19]}",
        "=" * 50,
    ])
    
    return "\n".join(lines)
