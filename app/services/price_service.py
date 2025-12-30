"""
Price Service
=============
Stock price fetching and caching using yfinance.
Designed for easy migration to Wix (all logic is pure functions).
"""

import yfinance as yf
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Simple in-memory cache
_price_cache: Dict[str, Tuple[float, datetime]] = {}
CACHE_DURATION = timedelta(minutes=5)


def get_stock_price(ticker: str, use_cache: bool = True) -> Optional[float]:
    """
    Get the current price for a stock ticker.
    
    Args:
        ticker: Stock symbol (e.g., 'AAPL', 'MSFT')
        use_cache: Whether to use cached price if available
        
    Returns:
        Current stock price or None if unavailable
        
    Example:
        >>> price = get_stock_price('AAPL')
        >>> print(f"Apple is trading at ${price:.2f}")
    """
    # Check cache first
    if use_cache and ticker in _price_cache:
        cached_price, cached_time = _price_cache[ticker]
        if datetime.now() - cached_time < CACHE_DURATION:
            return cached_price
    
    try:
        stock = yf.Ticker(ticker)
        price = None
        
        # Try fast_info first (fastest method)
        try:
            fast = stock.fast_info
            price = getattr(fast, 'last_price', None) or getattr(fast, 'regularMarketPrice', None)
        except:
            pass
        
        # Try getting from recent history if fast_info failed
        if price is None:
            try:
                hist = stock.history(period="5d")
                if not hist.empty:
                    price = float(hist['Close'].iloc[-1])
            except:
                pass
        
        # Fall back to info
        if price is None:
            try:
                info = stock.info
                price = info.get('regularMarketPrice') or info.get('currentPrice') or info.get('navPrice')
            except:
                pass
        
        if price:
            _price_cache[ticker] = (float(price), datetime.now())
            return float(price)
        return None
        
    except Exception as e:
        logger.error(f"Error fetching price for {ticker}: {e}")
        return None


def get_stock_info(ticker: str) -> Optional[Dict]:
    """
    Get detailed information about a stock.
    
    Args:
        ticker: Stock symbol
        
    Returns:
        Dictionary with stock info or None
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'ticker': ticker,
            'name': info.get('longName') or info.get('shortName', ticker),
            'price': info.get('regularMarketPrice') or info.get('currentPrice'),
            'currency': info.get('currency', 'USD'),
            'exchange': info.get('exchange'),
            'sector': info.get('sector'),
            'industry': info.get('industry')
        }
    except Exception as e:
        logger.error(f"Error fetching info for {ticker}: {e}")
        return None


def get_historical_data(ticker: str, period: str = "1y") -> Optional[Dict]:
    """
    Get historical price data for calculating ATH.
    
    Args:
        ticker: Stock symbol
        period: Time period ('1mo', '3mo', '6mo', '1y', '2y', '5y', 'max')
        
    Returns:
        Dictionary with historical data
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        
        if hist.empty:
            return None
            
        return {
            'ticker': ticker,
            'period': period,
            'high': float(hist['High'].max()),
            'low': float(hist['Low'].min()),
            'current': float(hist['Close'].iloc[-1]),
            'data_points': len(hist),
            'start_date': hist.index[0].strftime('%Y-%m-%d'),
            'end_date': hist.index[-1].strftime('%Y-%m-%d')
        }
    except Exception as e:
        logger.error(f"Error fetching historical data for {ticker}: {e}")
        return None


def calculate_ath_and_drawdown(ticker: str, period: str = "1y") -> Optional[Dict]:
    """
    Calculate All-Time High (within period) and current drawdown.
    
    This is a core function for Tom Lee's DCA strategy - the drawdown
    from ATH determines the investment multiplier.
    
    Args:
        ticker: Stock symbol
        period: Lookback period for ATH calculation
        
    Returns:
        Dictionary with ATH, current price, and drawdown percentage
        
    Example:
        >>> result = calculate_ath_and_drawdown('^GSPC')
        >>> print(f"S&P 500 is {result['drawdown_percent']:.1f}% below ATH")
    """
    hist_data = get_historical_data(ticker, period)
    
    if not hist_data:
        return None
    
    ath = hist_data['high']
    current = hist_data['current']
    drawdown = ((ath - current) / ath) * 100
    
    return {
        'ticker': ticker,
        'ath': round(ath, 2),
        'current': round(current, 2),
        'drawdown_percent': round(drawdown, 2),
        'period': period
    }


def get_batch_prices(tickers: list) -> Dict[str, Optional[float]]:
    """
    Get prices for multiple tickers efficiently.
    
    Args:
        tickers: List of stock symbols
        
    Returns:
        Dictionary mapping ticker to price
    """
    results = {}
    for ticker in tickers:
        results[ticker] = get_stock_price(ticker)
    return results


def clear_cache():
    """Clear the price cache."""
    global _price_cache
    _price_cache = {}


def validate_ticker(ticker: str) -> bool:
    """
    Check if a ticker symbol is valid.
    
    Args:
        ticker: Stock symbol to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        stock = yf.Ticker(ticker)
        # Try fast_info first (faster and more reliable)
        try:
            fast = stock.fast_info
            if hasattr(fast, 'last_price') and fast.last_price is not None:
                return True
            if hasattr(fast, 'regularMarketPrice') and fast.regularMarketPrice is not None:
                return True
        except:
            pass
        
        # Fall back to getting history (most reliable check)
        hist = stock.history(period="5d")
        if not hist.empty:
            return True
            
        # Last resort - check info
        info = stock.info
        if info.get('regularMarketPrice') is not None or info.get('currentPrice') is not None:
            return True
        # Some ETFs/funds use 'navPrice'
        if info.get('navPrice') is not None:
            return True
            
        return False
    except Exception as e:
        logger.error(f"Error validating ticker {ticker}: {e}")
        return False
