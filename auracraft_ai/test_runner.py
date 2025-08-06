#!/usr/bin/env python3
"""
AuraCraft AI Test Runner
Simple script to run all tests and provide clear feedback
"""

import subprocess
import sys
import os
import signal
import threading
from datetime import datetime

def run_command(cmd, description, timeout_seconds=30):
    """Run a command and return success status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=timeout_seconds)
        if result.returncode == 0:
            print(f"✅ {description} - PASSED")
            return True
        else:
            print(f"❌ {description} - FAILED")
            if result.stdout:
                print(f"STDOUT: {result.stdout}")
            if result.stderr:
                print(f"STDERR: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"❌ {description} - TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False

def test_app_import():
    """Test app import without using shell timeout"""
    print(f"\n🔄 App Import Test...")
    try:
        # Import test
        import app_simple
        print(f"✅ App Import Test - PASSED")
        return True
    except Exception as e:
        print(f"❌ App Import Test - FAILED: {e}")
        return False

def main():
    """Main test runner"""
    print("="*60)
    print("🚀 AURACRAFT AI - E2E TEST EXECUTION")
    print("="*60)
    print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Ensure we're in the right directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Unit tests for data parser
    total_tests += 1
    if run_command("python -m pytest test_e2e_comprehensive.py::TestDataParser -v", 
                   "Data Parser Unit Tests"):
        tests_passed += 1
    
    # Test 2: Unit tests for Google Sheets utils
    total_tests += 1
    if run_command("python -m pytest test_e2e_comprehensive.py::TestGoogleSheetsUtils -v", 
                   "Google Sheets Utils Tests"):
        tests_passed += 1
    
    # Test 3: LLM utils tests (with mocking)
    total_tests += 1
    if run_command("python -m pytest test_e2e_comprehensive.py::TestLLMUtils -v", 
                   "LLM Utils Tests"):
        tests_passed += 1
    
    # Test 4: Configuration tests
    total_tests += 1
    if run_command("python -m pytest test_e2e_comprehensive.py::TestConfiguration -v", 
                   "Configuration Tests"):
        tests_passed += 1
    
    # Test 5: Error handling tests
    total_tests += 1
    if run_command("python -m pytest test_e2e_comprehensive.py::TestErrorHandling -v", 
                   "Error Handling Tests"):
        tests_passed += 1
    
    # Test 6: Performance tests
    total_tests += 1
    if run_command("python -m pytest test_e2e_comprehensive.py::TestPerformanceAndStress -v", 
                   "Performance Tests"):
        tests_passed += 1
    
    # Test 7: App import test (Python-based, no shell timeout)
    total_tests += 1
    if test_app_import():
        tests_passed += 1
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST EXECUTION SUMMARY")
    print("="*60)
    print(f"✅ Tests Passed: {tests_passed}/{total_tests}")
    print(f"❌ Tests Failed: {total_tests - tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("🎉 ALL TESTS PASSED! AuraCraft AI is working correctly.")
        return 0
    else:
        print("⚠️  SOME TESTS FAILED. Please review the output above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 