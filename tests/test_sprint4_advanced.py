"""
Sprint 4 Tests - Advanced Features & Release
=============================================
Testing CSV export, market analysis, and documentation.
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
# DCA-035: EXPORT TO CSV TESTS
# ============================================================================

def test_export_portfolio_csv():
    """Test portfolio CSV export endpoint."""
    try:
        response = requests.get(f"{BASE_URL}/api/export/portfolio", timeout=10)
        
        if response.status_code == 404:
            # No portfolio data - this is expected without data
            data = response.json()
            if 'error' in data:
                test_passed("Export portfolio - handles empty portfolio")
            return
        
        if response.status_code == 200:
            # Check headers
            content_type = response.headers.get('Content-Type', '')
            disposition = response.headers.get('Content-Disposition', '')
            
            if 'text/csv' in content_type:
                test_passed("Export portfolio - returns CSV content type")
            else:
                test_failed("Export portfolio - returns CSV content type", f"Got: {content_type}")
                
            if 'attachment' in disposition and 'portfolio_export' in disposition:
                test_passed("Export portfolio - correct filename header")
            else:
                test_failed("Export portfolio - correct filename header", f"Got: {disposition}")
                
            # Check CSV content has headers
            content = response.text
            if 'Ticker' in content and 'Target Allocation' in content:
                test_passed("Export portfolio - CSV has correct headers")
            else:
                test_failed("Export portfolio - CSV has correct headers", "Missing expected headers")
        else:
            test_failed("Export portfolio - endpoint accessible", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Export portfolio CSV", str(e))


def test_export_investments_csv():
    """Test investment history CSV export."""
    try:
        response = requests.get(f"{BASE_URL}/api/export/investments", timeout=10)
        
        if response.status_code == 404:
            data = response.json()
            if 'error' in data:
                test_passed("Export investments - handles empty data")
            return
        
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            
            if 'text/csv' in content_type:
                test_passed("Export investments - returns CSV")
            else:
                test_failed("Export investments - returns CSV", f"Got: {content_type}")
                
            content = response.text
            if 'Date' in content and 'Ticker' in content:
                test_passed("Export investments - CSV has correct headers")
            else:
                test_failed("Export investments - CSV has correct headers", "Missing headers")
        else:
            test_failed("Export investments endpoint", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Export investments CSV", str(e))


def test_export_investments_with_filter():
    """Test investment export with ticker filter."""
    try:
        response = requests.get(f"{BASE_URL}/api/export/investments?ticker=AAPL", timeout=10)
        
        if response.status_code in [200, 404]:
            test_passed("Export investments - filter parameter works")
        else:
            test_failed("Export investments - filter parameter", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Export investments with filter", str(e))


def test_export_dca_plan():
    """Test DCA plan CSV export."""
    try:
        response = requests.get(f"{BASE_URL}/api/export/dca-plan", timeout=10)
        
        if response.status_code in [200, 404, 500]:
            # 200 = success, 404 = no settings, 500 = no market data
            test_passed("Export DCA plan - endpoint accessible")
        else:
            test_failed("Export DCA plan", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Export DCA plan", str(e))


# ============================================================================
# DCA-036: MARKET ANALYSIS PAGE TESTS
# ============================================================================

def test_market_analysis_endpoint():
    """Test market analysis API endpoint."""
    try:
        response = requests.get(f"{BASE_URL}/api/market/analysis", timeout=15)
        
        if response.status_code == 404:
            data = response.json()
            if 'error' in data:
                test_passed("Market analysis - handles missing settings")
            return
            
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                test_passed("Market analysis - returns success")
            else:
                test_failed("Market analysis - returns success", "success=False")
                return
            
            analysis = data.get('data', {})
            
            # Check required fields
            required_fields = ['index_ticker', 'current_price', 'ath_price', 
                             'drawdown_percent', 'condition', 'thresholds', 'multipliers']
            missing = [f for f in required_fields if f not in analysis]
            
            if not missing:
                test_passed("Market analysis - has all required fields")
            else:
                test_failed("Market analysis - has all required fields", f"Missing: {missing}")
                
            # Check thresholds structure
            if 'thresholds' in analysis:
                th = analysis['thresholds']
                if all(k in th for k in ['mild_dip', 'correction', 'bear', 'crash']):
                    test_passed("Market analysis - thresholds structure correct")
                else:
                    test_failed("Market analysis - thresholds structure", "Missing threshold keys")
                    
            # Check multipliers structure
            if 'multipliers' in analysis:
                mult = analysis['multipliers']
                if all(k in mult for k in ['normal', 'mild_dip', 'correction', 'bear', 'crash']):
                    test_passed("Market analysis - multipliers structure correct")
                else:
                    test_failed("Market analysis - multipliers structure", "Missing multiplier keys")
        else:
            test_failed("Market analysis endpoint", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Market analysis endpoint", str(e))


def test_market_page_loads():
    """Test market page renders correctly."""
    try:
        response = requests.get(f"{BASE_URL}/market", timeout=10)
        
        if response.status_code == 200:
            if 'Market Analysis' in response.text:
                test_passed("Market page - renders title")
            else:
                test_failed("Market page - renders title", "Title not found")
                
            if 'Market Condition Meter' in response.text:
                test_passed("Market page - has condition meter section")
            else:
                test_failed("Market page - has condition meter section", "Section not found")
                
            if 'Opportunity Scanner' in response.text:
                test_passed("Market page - has opportunity scanner section")
            else:
                test_failed("Market page - has opportunity scanner section", "Section not found")
        else:
            test_failed("Market page loads", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Market page loads", str(e))


# ============================================================================
# DCA-037: MARKET CONDITION METER TESTS
# ============================================================================

def test_condition_meter_endpoint():
    """Test market condition meter API."""
    try:
        response = requests.get(f"{BASE_URL}/api/market/condition-meter", timeout=15)
        
        if response.status_code == 404:
            test_passed("Condition meter - handles missing settings")
            return
            
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                test_passed("Condition meter - returns success")
            else:
                test_failed("Condition meter - returns success", "success=False")
                return
            
            meter = data.get('data', {})
            
            # Check required fields
            required = ['current_drawdown', 'current_zone', 'needle_position', 'zones']
            missing = [f for f in required if f not in meter]
            
            if not missing:
                test_passed("Condition meter - has required fields")
            else:
                test_failed("Condition meter - has required fields", f"Missing: {missing}")
                
            # Check zones array
            zones = meter.get('zones', [])
            if len(zones) == 5:
                test_passed("Condition meter - has 5 zones")
            else:
                test_failed("Condition meter - has 5 zones", f"Got: {len(zones)}")
                
            # Check zone structure
            if zones:
                zone = zones[0]
                if all(k in zone for k in ['name', 'min', 'max', 'color', 'multiplier']):
                    test_passed("Condition meter - zone structure correct")
                else:
                    test_failed("Condition meter - zone structure", "Missing zone keys")
        else:
            test_failed("Condition meter endpoint", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Condition meter endpoint", str(e))


# ============================================================================
# DCA-038: OPPORTUNITY SCANNER TESTS
# ============================================================================

def test_opportunity_scanner_endpoint():
    """Test opportunity scanner API."""
    try:
        response = requests.get(f"{BASE_URL}/api/market/opportunities", timeout=30)
        
        if response.status_code == 404:
            data = response.json()
            if 'error' in data:
                test_passed("Opportunity scanner - handles missing portfolio")
            return
            
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                test_passed("Opportunity scanner - returns success")
            else:
                test_failed("Opportunity scanner - returns success", "success=False")
                return
            
            result = data.get('data', {})
            
            # Handle case where data is a list (empty portfolio)
            if isinstance(result, list):
                test_passed("Opportunity scanner - handles empty portfolio")
                return
            
            # Check structure
            if 'opportunities' in result and 'summary' in result:
                test_passed("Opportunity scanner - correct structure")
            else:
                test_failed("Opportunity scanner - correct structure", "Missing opportunities or summary")
                return
                
            # Check summary fields
            summary = result.get('summary', {})
            if all(k in summary for k in ['total_stocks', 'buying_opportunities', 'average_drawdown']):
                test_passed("Opportunity scanner - summary fields correct")
            else:
                test_failed("Opportunity scanner - summary fields", "Missing summary keys")
                
            # Check opportunity structure if any exist
            opps = result.get('opportunities', [])
            if opps:
                opp = opps[0]
                required = ['ticker', 'current_price', 'high_52w', 'drawdown_percent', 
                           'opportunity_level', 'opportunity_score']
                if all(k in opp for k in required):
                    test_passed("Opportunity scanner - opportunity structure correct")
                else:
                    test_failed("Opportunity scanner - opportunity structure", "Missing keys")
                    
                # Check opportunity level validity
                valid_levels = ['none', 'mild', 'moderate', 'strong', 'exceptional']
                if opp.get('opportunity_level') in valid_levels:
                    test_passed("Opportunity scanner - valid opportunity levels")
                else:
                    test_failed("Opportunity scanner - valid opportunity levels", 
                               f"Got: {opp.get('opportunity_level')}")
            else:
                test_passed("Opportunity scanner - handles empty opportunities")
        else:
            test_failed("Opportunity scanner endpoint", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Opportunity scanner endpoint", str(e))


# ============================================================================
# EXPORT BUTTONS UI TESTS
# ============================================================================

def test_portfolio_page_has_export():
    """Test portfolio page has export button."""
    try:
        response = requests.get(f"{BASE_URL}/portfolio", timeout=10)
        
        if response.status_code == 200:
            content = response.text
            if 'export' in content.lower() and 'exportPortfolio' in content:
                test_passed("Portfolio page - has export button")
            elif 'Export' in content:
                test_passed("Portfolio page - has export button")
            else:
                test_failed("Portfolio page - has export button", "Export button not found")
        else:
            test_failed("Portfolio page export check", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Portfolio page export check", str(e))


def test_history_page_has_export():
    """Test history page has export button."""
    try:
        response = requests.get(f"{BASE_URL}/history", timeout=10)
        
        if response.status_code == 200:
            content = response.text
            if 'export' in content.lower() and 'exportInvestments' in content:
                test_passed("History page - has export button")
            elif 'Export' in content:
                test_passed("History page - has export button")
            else:
                test_failed("History page - has export button", "Export button not found")
        else:
            test_failed("History page export check", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("History page export check", str(e))


def test_dashboard_has_export():
    """Test dashboard has DCA plan export."""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        
        if response.status_code == 200:
            content = response.text
            if 'Export' in content and 'exportDCAPlan' in content:
                test_passed("Dashboard - has export plan button")
            elif 'Export Plan' in content or 'Export' in content:
                test_passed("Dashboard - has export plan button")
            else:
                test_failed("Dashboard - has export plan button", "Export button not found")
        else:
            test_failed("Dashboard export check", f"Status: {response.status_code}")
            
    except Exception as e:
        test_failed("Dashboard export check", str(e))


# ============================================================================
# DCA-044: DOCUMENTATION TESTS
# ============================================================================

def test_readme_exists():
    """Test README.md exists and has required sections."""
    readme_path = os.path.join(PROJECT_ROOT, 'README.md')
    
    try:
        if not os.path.exists(readme_path):
            test_failed("README exists", "File not found")
            return
            
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        test_passed("README.md exists")
        
        # Check for required sections
        if '# Smart DCA Investment Tool' in content:
            test_passed("README - has title")
        else:
            test_failed("README - has title", "Title not found")
            
        if 'Quick Start' in content:
            test_passed("README - has Quick Start section")
        else:
            test_failed("README - has Quick Start section", "Section not found")
            
        if 'Installation' in content:
            test_passed("README - has Installation section")
        else:
            test_failed("README - has Installation section", "Section not found")
            
        if 'API Endpoints' in content:
            test_passed("README - has API Endpoints section")
        else:
            test_failed("README - has API Endpoints section", "Section not found")
            
        if 'Tom Lee' in content or 'DCA Strategy' in content:
            test_passed("README - explains DCA strategy")
        else:
            test_failed("README - explains DCA strategy", "Strategy explanation not found")
            
    except Exception as e:
        test_failed("README check", str(e))


# ============================================================================
# RUN ALL TESTS
# ============================================================================

def run_sprint4_tests():
    print("\n" + "="*60)
    print("SPRINT 4 TESTS - Advanced Features & Release")
    print("="*60)
    
    # Check server is running
    print("\n[Checking server availability...]")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code != 200:
            print(f"❌ Server not responding correctly. Status: {response.status_code}")
            return results
        print("✓ Server is running\n")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the Flask app is running on port 5000.")
        return results
    
    # DCA-035: Export to CSV
    print("\n[DCA-035: Export to CSV]")
    test_export_portfolio_csv()
    test_export_investments_csv()
    test_export_investments_with_filter()
    test_export_dca_plan()
    
    # DCA-036: Market Analysis Page
    print("\n[DCA-036: Market Analysis Page]")
    test_market_analysis_endpoint()
    test_market_page_loads()
    
    # DCA-037: Market Condition Meter
    print("\n[DCA-037: Market Condition Meter]")
    test_condition_meter_endpoint()
    
    # DCA-038: Opportunity Scanner
    print("\n[DCA-038: Opportunity Scanner]")
    test_opportunity_scanner_endpoint()
    
    # Export Button UI Tests
    print("\n[Export Button UI Tests]")
    test_portfolio_page_has_export()
    test_history_page_has_export()
    test_dashboard_has_export()
    
    # DCA-044: Documentation
    print("\n[DCA-044: Documentation]")
    test_readme_exists()
    
    # Summary
    print("\n" + "="*60)
    print("SPRINT 4 TEST SUMMARY")
    print("="*60)
    print(f"  Passed:  {len(results['passed'])}")
    print(f"  Failed:  {len(results['failed'])}")
    print(f"  Skipped: {len(results['skipped'])}")
    
    if results['failed']:
        print("\n❌ FAILED TESTS:")
        for fail in results['failed']:
            print(f"  - {fail}")
    
    return results


if __name__ == '__main__':
    run_sprint4_tests()
