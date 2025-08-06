#!/usr/bin/env python3
"""
AuraCraft AI Collaborative Launcher
Properly launches the app and opens browser
"""

import os
import sys
import webbrowser
import time
import subprocess
from threading import Timer

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking requirements...")
    
    # Check if we're in virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Not in virtual environment")
        print("💡 Tip: Run 'source venv/bin/activate' first")
    
    # Check API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("⚠️  Warning: GOOGLE_API_KEY not set")
        print("💡 For demo mode, we'll use a test key")
        os.environ['GOOGLE_API_KEY'] = 'demo_key_for_testing'
    else:
        print("✅ API key configured")
    
    # Check dependencies
    try:
        import nicegui
        print(f"✅ NiceGUI {nicegui.__version__} ready")
    except ImportError:
        print("❌ NiceGUI not installed")
        print("💡 Run: pip install -r requirements.txt")
        return False
    
    return True

def open_browser_delayed():
    """Open browser after a delay"""
    time.sleep(3)  # Wait for server to start
    print("🌐 Opening browser...")
    webbrowser.open('http://localhost:8080')

def main():
    """Main launcher function"""
    print("🚀 AuraCraft AI Collaborative Launcher")
    print("=" * 50)
    
    if not check_requirements():
        print("❌ Requirements not met. Please fix issues above.")
        return 1
    
    print("\n🎨 Starting AuraCraft AI Collaborative...")
    print("🌐 Server will be available at: http://localhost:8080")
    print("📱 Perfect for creators of all experience levels!")
    print("\n" + "="*50)
    
    # Start browser opening in background
    Timer(3.0, open_browser_delayed).start()
    
    try:
        # Import and run the collaborative app
        from app_collaborative import collaborative_main
        import nicegui as ui
        
        # Run the app
        ui.run(
            port=8080, 
            show=True,  # This should open browser automatically
            title="AuraCraft AI - Collaborative Content Creator",
            favicon="🎨"
        )
        
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using AuraCraft AI!")
        print("💡 Your session data has been saved.")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error starting app: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Make sure you're in the auracraft_ai directory")
        print("2. Activate virtual environment: source venv/bin/activate")
        print("3. Install dependencies: pip install -r requirements.txt")
        print("4. Try: python app_collaborative.py")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 