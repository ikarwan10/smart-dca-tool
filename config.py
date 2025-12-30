"""
Smart DCA Investment Tool - Configuration
==========================================
Application configuration settings for different environments.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the base directory for the app
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class."""
    
    # Flask Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database Settings - use absolute path
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'dca_tool.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application Settings
    APP_NAME = 'Smart DCA Investment Tool'
    APP_VERSION = '1.0.0'
    
    # DCA Strategy Defaults (Based on Tom Lee's Strategy)
    DEFAULT_BASE_INVESTMENT = 500.0  # Default monthly investment amount
    DEFAULT_INDEX_TICKER = '^GSPC'   # S&P 500 for market condition
    
    # Market Condition Thresholds (% below ATH)
    MARKET_THRESHOLDS = {
        'normal': 0,           # At or near ATH: 1.0x multiplier
        'mild_dip': 5,         # 5-10% below ATH: 1.5x multiplier
        'correction': 10,      # 10-20% below ATH: 2.0x multiplier
        'bear': 20,            # 20-30% below ATH: 2.5x multiplier
        'crash': 30,           # 30%+ below ATH: 3.0x multiplier
    }
    
    # Investment Multipliers
    MULTIPLIERS = {
        'normal': 1.0,
        'mild_dip': 1.5,
        'correction': 2.0,
        'bear': 2.5,
        'crash': 3.0,
    }
    
    # Price Cache Duration (seconds)
    PRICE_CACHE_DURATION = 300  # 5 minutes


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Log SQL queries


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
