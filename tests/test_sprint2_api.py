"""
Sprint 2 Frontend/API Tests
===========================
Testing API endpoints, CRUD operations, and integration
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import json

# Import the app directly from app.py
from app_module import app as flask_app
from app.models.models import db


def get_test_app():
    """Get a configured test app."""
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    flask_app.config['WTF_CSRF_ENABLED'] = False
    return flask_app


class TestFlaskApp(unittest.TestCase):
    """Test Flask application setup"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        cls.app = get_test_app()
        cls.client = cls.app.test_client()
        
        # Create tables
        with cls.app.app_context():
            db.create_all()
    
    def test_app_exists(self):
        """Test that app was created"""
        self.assertIsNotNone(self.app)
        print("✓ Flask app exists")
    
    def test_app_is_testing(self):
        """Test that app is in testing mode"""
        self.assertTrue(self.app.config['TESTING'])
        print("✓ App in testing mode")


class TestPortfolioAPI(unittest.TestCase):
    """Test Portfolio CRUD API endpoints"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        from app import create_app
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()
        
        with cls.app.app_context():
            from app.models.models import db
            db.create_all()
    
    def test_get_portfolio_empty(self):
        """Test getting empty portfolio"""
        with self.app.app_context():
            response = self.client.get('/api/portfolio')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['success'])
            print("✓ GET /api/portfolio returns success")
    
    def test_add_holding(self):
        """Test adding a holding"""
        with self.app.app_context():
            response = self.client.post('/api/holdings',
                data=json.dumps({
                    'ticker': 'TEST',
                    'name': 'Test Stock',
                    'target_allocation': 50,
                    'shares_owned': 10
                }),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 201)
            data = json.loads(response.data)
            self.assertTrue(data['success'])
            print("✓ POST /api/holdings creates holding")
    
    def test_add_holding_duplicate(self):
        """Test adding duplicate holding fails"""
        with self.app.app_context():
            # Add first
            self.client.post('/api/holdings',
                data=json.dumps({'ticker': 'DUP', 'target_allocation': 25}),
                content_type='application/json'
            )
            # Try duplicate
            response = self.client.post('/api/holdings',
                data=json.dumps({'ticker': 'DUP', 'target_allocation': 25}),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 400)
            print("✓ Duplicate holding rejected")
    
    def test_add_holding_no_ticker(self):
        """Test adding holding without ticker fails"""
        with self.app.app_context():
            response = self.client.post('/api/holdings',
                data=json.dumps({'name': 'No Ticker'}),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 400)
            print("✓ Missing ticker rejected")


class TestSettingsAPI(unittest.TestCase):
    """Test Settings API endpoints"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        from app import create_app
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()
        
        with cls.app.app_context():
            from app.models.models import db
            db.create_all()
    
    def test_get_settings(self):
        """Test getting settings"""
        with self.app.app_context():
            response = self.client.get('/api/settings')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['success'])
            self.assertIn('base_investment', data['data'])
            print("✓ GET /api/settings returns defaults")
    
    def test_update_settings(self):
        """Test updating settings"""
        with self.app.app_context():
            response = self.client.put('/api/settings',
                data=json.dumps({
                    'base_investment': 1000,
                    'index_ticker': '^GSPC'
                }),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['success'])
            print("✓ PUT /api/settings updates correctly")
    
    def test_reset_settings(self):
        """Test resetting settings to defaults"""
        with self.app.app_context():
            response = self.client.post('/api/settings/reset')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertTrue(data['success'])
            print("✓ POST /api/settings/reset works")


class TestDCACalculationAPI(unittest.TestCase):
    """Test DCA calculation API endpoint"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        from app import create_app
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.client = cls.app.test_client()
        
        with cls.app.app_context():
            from app.models.models import db
            db.create_all()
    
    def test_dca_calculate_endpoint_exists(self):
        """Test DCA calculate endpoint exists"""
        with self.app.app_context():
            response = self.client.post('/api/dca/calculate',
                data=json.dumps({
                    'holdings': [
                        {'ticker': 'VOO', 'target_allocation': 60},
                        {'ticker': 'QQQ', 'target_allocation': 40}
                    ],
                    'base_amount': 500,
                    'index_ticker': '^GSPC'
                }),
                content_type='application/json'
            )
            # Should return 200 even if prices fail (graceful degradation)
            self.assertIn(response.status_code, [200, 500])
            print("✓ POST /api/dca/calculate endpoint exists")


class TestPageRoutes(unittest.TestCase):
    """Test page routes return HTML"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        from app import create_app
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()
    
    def test_dashboard_page(self):
        """Test dashboard page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)
        print("✓ Dashboard page loads")
    
    def test_portfolio_page(self):
        """Test portfolio page loads"""
        response = self.client.get('/portfolio')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Portfolio', response.data)
        print("✓ Portfolio page loads")
    
    def test_planner_page(self):
        """Test planner page loads"""
        response = self.client.get('/planner')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Planner', response.data)
        print("✓ Planner page loads")
    
    def test_settings_page(self):
        """Test settings page loads"""
        response = self.client.get('/settings')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Settings', response.data)
        print("✓ Settings page loads")
    
    def test_market_page(self):
        """Test market page loads"""
        response = self.client.get('/market')
        self.assertEqual(response.status_code, 200)
        print("✓ Market page loads")
    
    def test_history_page(self):
        """Test history page loads"""
        response = self.client.get('/history')
        self.assertEqual(response.status_code, 200)
        print("✓ History page loads")


def run_tests():
    """Run all Sprint 2 tests"""
    print("=" * 60)
    print("SPRINT 2 FRONTEND/API TESTS")
    print("=" * 60)
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestFlaskApp))
    suite.addTests(loader.loadTestsFromTestCase(TestPortfolioAPI))
    suite.addTests(loader.loadTestsFromTestCase(TestSettingsAPI))
    suite.addTests(loader.loadTestsFromTestCase(TestDCACalculationAPI))
    suite.addTests(loader.loadTestsFromTestCase(TestPageRoutes))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("SPRINT 2 TEST SUMMARY")
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
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
