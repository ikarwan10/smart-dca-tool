"""
Sprint 1 Backend Tests
======================
Testing core backend functionality: models, services, calculations
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import datetime

# Test results collector
results = {
    'passed': [],
    'failed': [],
    'skipped': []
}


class TestDCAEngine(unittest.TestCase):
    """Test DCA calculation engine - core business logic"""
    
    def test_market_condition_normal(self):
        """Test normal market condition (0-5% below ATH)"""
        from app.services.dca_engine import determine_market_condition
        
        # 2% below ATH = Normal
        condition = determine_market_condition(2.0)
        self.assertEqual(condition, 'normal')
        results['passed'].append('DCA Engine: Normal market condition')
    
    def test_market_condition_mild_dip(self):
        """Test mild dip condition (5-10% below ATH)"""
        from app.services.dca_engine import determine_market_condition
        
        condition = determine_market_condition(7.0)
        self.assertEqual(condition, 'mild_dip')
        results['passed'].append('DCA Engine: Mild dip condition')
    
    def test_market_condition_correction(self):
        """Test correction condition (10-20% below ATH)"""
        from app.services.dca_engine import determine_market_condition
        
        condition = determine_market_condition(15.0)
        self.assertEqual(condition, 'correction')
        results['passed'].append('DCA Engine: Correction condition')
    
    def test_market_condition_bear(self):
        """Test bear market condition (20-30% below ATH)"""
        from app.services.dca_engine import determine_market_condition
        
        condition = determine_market_condition(25.0)
        self.assertEqual(condition, 'bear')
        results['passed'].append('DCA Engine: Bear market condition')
    
    def test_market_condition_crash(self):
        """Test crash condition (30%+ below ATH)"""
        from app.services.dca_engine import determine_market_condition
        
        condition = determine_market_condition(35.0)
        self.assertEqual(condition, 'crash')
        results['passed'].append('DCA Engine: Crash condition')
    
    def test_multiplier_calculation(self):
        """Test investment multiplier calculation"""
        from app.services.dca_engine import get_multiplier
        
        self.assertEqual(get_multiplier('normal'), 1.0)
        self.assertEqual(get_multiplier('mild_dip'), 1.5)
        self.assertEqual(get_multiplier('correction'), 2.0)
        self.assertEqual(get_multiplier('bear'), 2.5)
        self.assertEqual(get_multiplier('crash'), 3.0)
        results['passed'].append('DCA Engine: Multiplier calculation')
    
    def test_investment_amount_calculation(self):
        """Test total investment amount calculation"""
        from app.services.dca_engine import calculate_investment_amount
        
        # Base $500, normal market = $500
        amount = calculate_investment_amount(500, 'normal')
        self.assertEqual(amount, 500)
        
        # Base $500, correction = $1000
        amount = calculate_investment_amount(500, 'correction')
        self.assertEqual(amount, 1000)
        
        # Base $500, crash = $1500
        amount = calculate_investment_amount(500, 'crash')
        self.assertEqual(amount, 1500)
        
        results['passed'].append('DCA Engine: Investment amount calculation')
    
    def test_allocation_calculation(self):
        """Test per-stock allocation calculation"""
        from app.services.dca_engine import calculate_allocations
        
        holdings = [
            {'ticker': 'VOO', 'target_allocation': 60},
            {'ticker': 'QQQ', 'target_allocation': 40}
        ]
        
        allocations = calculate_allocations(holdings, 1000)
        
        self.assertEqual(len(allocations), 2)
        self.assertEqual(allocations[0]['amount'], 600)
        self.assertEqual(allocations[1]['amount'], 400)
        results['passed'].append('DCA Engine: Allocation calculation')


class TestDatabaseModels(unittest.TestCase):
    """Test database models"""
    
    def test_portfolio_model_exists(self):
        """Test Portfolio model can be imported"""
        from app.models.models import Portfolio
        self.assertIsNotNone(Portfolio)
        results['passed'].append('Models: Portfolio model exists')
    
    def test_holding_model_exists(self):
        """Test Holding model can be imported"""
        from app.models.models import Holding
        self.assertIsNotNone(Holding)
        results['passed'].append('Models: Holding model exists')
    
    def test_settings_model_exists(self):
        """Test Settings model can be imported"""
        from app.models.models import Settings
        self.assertIsNotNone(Settings)
        results['passed'].append('Models: Settings model exists')
    
    def test_investment_log_model_exists(self):
        """Test InvestmentLog model can be imported"""
        from app.models.models import InvestmentLog
        self.assertIsNotNone(InvestmentLog)
        results['passed'].append('Models: InvestmentLog model exists')


class TestPriceService(unittest.TestCase):
    """Test price service - with mocking to avoid API rate limits"""
    
    def test_price_service_imports(self):
        """Test price service can be imported"""
        from app.services import price_service
        self.assertIsNotNone(price_service.get_stock_price)
        self.assertIsNotNone(price_service.validate_ticker)
        self.assertIsNotNone(price_service.calculate_ath_and_drawdown)
        results['passed'].append('Price Service: Module imports correctly')
    
    def test_cache_mechanism(self):
        """Test that price cache exists"""
        from app.services import price_service
        # Check cache variable exists
        self.assertTrue(hasattr(price_service, '_price_cache'))
        results['passed'].append('Price Service: Cache mechanism exists')
    
    def test_clear_cache_function(self):
        """Test cache clearing function"""
        from app.services import price_service
        # This should not raise an error
        price_service.clear_price_cache()
        results['passed'].append('Price Service: Clear cache function works')


class TestMarketService(unittest.TestCase):
    """Test market analysis service"""
    
    def test_market_service_imports(self):
        """Test market service can be imported"""
        from app.services import market_service
        self.assertIsNotNone(market_service)
        results['passed'].append('Market Service: Module imports correctly')


def run_tests():
    """Run all tests and collect results"""
    print("=" * 60)
    print("SPRINT 1 BACKEND TESTS")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDCAEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestDatabaseModels))
    suite.addTests(loader.loadTestsFromTestCase(TestPriceService))
    suite.addTests(loader.loadTestsFromTestCase(TestMarketService))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("SPRINT 1 TEST SUMMARY")
    print("=" * 60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, trace in result.failures:
            print(f"  - {test}")
    
    if result.errors:
        print("\nERRORS:")
        for test, trace in result.errors:
            print(f"  - {test}")
            print(f"    {trace[:200]}...")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
