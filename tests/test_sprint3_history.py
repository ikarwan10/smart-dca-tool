"""
Sprint 3 Tests - History & Performance
======================================
Testing investment logging, history, and performance calculations.
"""

import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import requests
import json
from datetime import datetime, date, timedelta

# Test configuration
BASE_URL = "http://127.0.0.1:5000"

# Test results
results = {
    'passed': [],
    'failed': [],
    'skipped': []
}


def test_passed(name):
    results['passed'].append(name)
    print(f"  ✓ {name}")


def test_failed(name, error):
    results['failed'].append(f"{name}: {error}")
    print(f"  ✗ {name} - {error}")


def test_skipped(name, reason):
    results['skipped'].append(f"{name}: {reason}")
    print(f"  ⊘ {name} - {reason}")


# ============================================================================
# SPRINT 3 TESTS - Investment History & Performance
# ============================================================================

def run_sprint3_tests():
    print("\n" + "="*60)
    print("SPRINT 3 TESTS - Investment History & Performance")
    print("="*60)
    
    # Check server connectivity
    print("\n[3.0] Server Connectivity")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            test_passed("Server is running at localhost:5000")
        else:
            test_failed("Health check", f"Status {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        test_failed("Server connectivity", "Cannot connect to localhost:5000")
        print("  ⚠️  Make sure the Flask server is running!")
        return
    
    # Test 3.1: History Page
    print("\n[3.1] History Page Route")
    try:
        response = requests.get(f"{BASE_URL}/history", timeout=5)
        if response.status_code == 200:
            test_passed("GET /history returns 200")
            if 'Investment History' in response.text:
                test_passed("History page contains title")
        else:
            test_failed("GET /history", f"Status {response.status_code}")
    except Exception as e:
        test_failed("History page", str(e))
    
    # Test 3.2: Get Investments (Empty)
    print("\n[3.2] Investment API - GET (Initial)")
    try:
        response = requests.get(f"{BASE_URL}/api/investments", timeout=5)
        data = response.json()
        
        if response.status_code == 200 and data.get('success'):
            test_passed("GET /api/investments returns success")
            if 'investments' in data.get('data', {}):
                test_passed("Response contains investments array")
        else:
            test_failed("GET /api/investments", f"Response: {data}")
    except Exception as e:
        test_failed("GET /api/investments", str(e))
    
    # Test 3.3: Log Investment
    print("\n[3.3] Investment API - POST (Log Investment)")
    test_date = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    test_investment = {
        'ticker': 'TEST',
        'date': test_date,
        'shares': 10.5,
        'price': 100.00,
        'notes': 'Sprint 3 test investment',
        'market_condition': 'normal',
        'multiplier_used': 1.0,
        'update_holding': False
    }
    
    investment_id = None
    try:
        response = requests.post(
            f"{BASE_URL}/api/investments",
            json=test_investment,
            timeout=5
        )
        data = response.json()
        
        if response.status_code == 201 and data.get('success'):
            test_passed("POST /api/investments creates investment")
            
            inv_data = data.get('data', {})
            investment_id = inv_data.get('id')
            
            if inv_data.get('ticker') == 'TEST':
                test_passed("Investment has correct ticker")
            if inv_data.get('shares') == 10.5:
                test_passed("Investment has correct shares")
            if inv_data.get('total_amount') == 1050.0:
                test_passed("Total amount calculated correctly (10.5 * 100)")
        else:
            test_failed("POST /api/investments", f"Response: {data}")
    except Exception as e:
        test_failed("POST /api/investments", str(e))
    
    # Test 3.4: Get Investment by ID
    print("\n[3.4] Investment API - GET Single")
    if investment_id:
        try:
            response = requests.get(f"{BASE_URL}/api/investments/{investment_id}", timeout=5)
            data = response.json()
            
            if response.status_code == 200 and data.get('success'):
                test_passed(f"GET /api/investments/{investment_id} returns investment")
            else:
                test_failed("GET single investment", f"Response: {data}")
        except Exception as e:
            test_failed("GET single investment", str(e))
    else:
        test_skipped("GET single investment", "No investment ID from POST")
    
    # Test 3.5: Update Investment
    print("\n[3.5] Investment API - PUT (Update)")
    if investment_id:
        try:
            response = requests.put(
                f"{BASE_URL}/api/investments/{investment_id}",
                json={'shares': 15.0, 'notes': 'Updated notes'},
                timeout=5
            )
            data = response.json()
            
            if response.status_code == 200 and data.get('success'):
                test_passed(f"PUT /api/investments/{investment_id} updates investment")
                
                if data.get('data', {}).get('shares') == 15.0:
                    test_passed("Shares updated correctly")
                if data.get('data', {}).get('total_amount') == 1500.0:
                    test_passed("Total recalculated on update")
            else:
                test_failed("PUT investment", f"Response: {data}")
        except Exception as e:
            test_failed("PUT investment", str(e))
    else:
        test_skipped("PUT investment", "No investment ID")
    
    # Test 3.6: Filter Investments by Ticker
    print("\n[3.6] Investment API - Filter by Ticker")
    try:
        response = requests.get(f"{BASE_URL}/api/investments?ticker=TEST", timeout=5)
        data = response.json()
        
        if response.status_code == 200 and data.get('success'):
            test_passed("Filter by ticker works")
            
            investments = data.get('data', {}).get('investments', [])
            if all(inv['ticker'] == 'TEST' for inv in investments):
                test_passed("All filtered results have correct ticker")
        else:
            test_failed("Filter by ticker", f"Response: {data}")
    except Exception as e:
        test_failed("Filter by ticker", str(e))
    
    # Test 3.7: Investment Summary
    print("\n[3.7] Investment Summary API")
    try:
        response = requests.get(f"{BASE_URL}/api/investments/summary", timeout=30)
        data = response.json()
        
        if response.status_code == 200 and data.get('success'):
            test_passed("GET /api/investments/summary returns success")
            
            summary = data.get('data', {})
            if 'total_invested' in summary:
                test_passed("Summary contains total_invested")
            if 'by_ticker' in summary:
                test_passed("Summary contains by_ticker breakdown")
            if 'by_month' in summary:
                test_passed("Summary contains by_month data")
            if 'investment_count' in summary:
                test_passed("Summary contains investment_count")
        else:
            test_failed("Investment summary", f"Response: {data}")
    except Exception as e:
        test_failed("Investment summary", str(e))
    
    # Test 3.8: Chart Data API
    print("\n[3.8] Chart Data API")
    try:
        response = requests.get(f"{BASE_URL}/api/investments/chart-data", timeout=5)
        data = response.json()
        
        if response.status_code == 200 and data.get('success'):
            test_passed("GET /api/investments/chart-data returns success")
            
            chart_data = data.get('data', {})
            if 'labels' in chart_data:
                test_passed("Chart data contains labels")
            if 'invested' in chart_data:
                test_passed("Chart data contains invested values")
            if 'cumulative' in chart_data:
                test_passed("Chart data contains cumulative values")
        else:
            test_failed("Chart data", f"Response: {data}")
    except Exception as e:
        test_failed("Chart data", str(e))
    
    # Test 3.9: Validation - Invalid Investment
    print("\n[3.9] Investment Validation")
    try:
        # Test missing ticker
        response = requests.post(
            f"{BASE_URL}/api/investments",
            json={'shares': 10, 'price': 100},
            timeout=5
        )
        if response.status_code == 400:
            test_passed("Missing ticker rejected with 400")
        else:
            test_failed("Missing ticker validation", f"Status {response.status_code}")
        
        # Test negative shares
        response = requests.post(
            f"{BASE_URL}/api/investments",
            json={'ticker': 'TEST', 'shares': -5, 'price': 100},
            timeout=5
        )
        if response.status_code == 400:
            test_passed("Negative shares rejected with 400")
        else:
            test_failed("Negative shares validation", f"Status {response.status_code}")
        
        # Test invalid date
        response = requests.post(
            f"{BASE_URL}/api/investments",
            json={'ticker': 'TEST', 'shares': 10, 'price': 100, 'date': 'invalid'},
            timeout=5
        )
        if response.status_code == 400:
            test_passed("Invalid date format rejected with 400")
        else:
            test_failed("Invalid date validation", f"Status {response.status_code}")
            
    except Exception as e:
        test_failed("Investment validation", str(e))
    
    # Test 3.10: Delete Investment
    print("\n[3.10] Investment API - DELETE")
    if investment_id:
        try:
            response = requests.delete(f"{BASE_URL}/api/investments/{investment_id}", timeout=5)
            data = response.json()
            
            if response.status_code == 200 and data.get('success'):
                test_passed(f"DELETE /api/investments/{investment_id} removes investment")
                
                # Verify it's gone
                response = requests.get(f"{BASE_URL}/api/investments/{investment_id}", timeout=5)
                if response.status_code == 404:
                    test_passed("Deleted investment returns 404")
            else:
                test_failed("DELETE investment", f"Response: {data}")
        except Exception as e:
            test_failed("DELETE investment", str(e))
    else:
        test_skipped("DELETE investment", "No investment ID")
    
    # Test 3.11: Multiple Investments for Performance Calc
    print("\n[3.11] Multiple Investments Performance")
    try:
        # Create multiple test investments
        investments_created = []
        for i in range(3):
            inv_date = (date.today() - timedelta(days=30*i)).strftime('%Y-%m-%d')
            response = requests.post(
                f"{BASE_URL}/api/investments",
                json={
                    'ticker': 'PERFTEST',
                    'date': inv_date,
                    'shares': 5,
                    'price': 100 + (i * 10),
                    'update_holding': False
                },
                timeout=5
            )
            if response.status_code == 201:
                data = response.json()
                investments_created.append(data.get('data', {}).get('id'))
        
        if len(investments_created) == 3:
            test_passed("Created 3 test investments for performance")
            
            # Check summary calculations
            response = requests.get(f"{BASE_URL}/api/investments/summary", timeout=30)
            data = response.json()
            
            if data.get('success'):
                ticker_data = data.get('data', {}).get('by_ticker', {}).get('PERFTEST', {})
                if ticker_data:
                    if ticker_data.get('total_shares') == 15:
                        test_passed("Total shares calculated correctly (5 * 3 = 15)")
                    expected_invested = (5*100) + (5*110) + (5*120)  # 1650
                    if ticker_data.get('total_invested') == expected_invested:
                        test_passed(f"Total invested calculated correctly (${expected_invested})")
                    
                    avg_cost = expected_invested / 15  # 110
                    if abs(ticker_data.get('avg_cost', 0) - avg_cost) < 0.01:
                        test_passed(f"Average cost calculated correctly (${avg_cost})")
        
        # Cleanup
        for inv_id in investments_created:
            if inv_id:
                requests.delete(f"{BASE_URL}/api/investments/{inv_id}", timeout=5)
        
    except Exception as e:
        test_failed("Multiple investments performance", str(e))


# ============================================================================
# REPORT GENERATION
# ============================================================================

def generate_report():
    print("\n" + "="*60)
    print("SPRINT 3 TEST RESULTS SUMMARY")
    print("="*60)
    
    passed = len(results['passed'])
    failed = len(results['failed'])
    skipped = len(results['skipped'])
    
    print(f"\n  ✓ Passed:  {passed}")
    print(f"  ✗ Failed:  {failed}")
    print(f"  ⊘ Skipped: {skipped}")
    
    if failed > 0:
        print(f"\n  Failed tests:")
        for fail in results['failed']:
            print(f"    - {fail}")
    
    print("\n" + "-"*60)
    print(f"TOTAL: {passed} passed, {failed} failed, {skipped} skipped")
    print("-"*60)
    
    if failed == 0:
        print("\n🎉 ALL SPRINT 3 TESTS PASSED! 🎉")
    else:
        print(f"\n⚠️  {failed} test(s) need attention")
    
    return failed == 0


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("DCA TOOL - SPRINT 3 VALIDATION TEST SUITE")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    run_sprint3_tests()
    success = generate_report()
    
    sys.exit(0 if success else 1)
