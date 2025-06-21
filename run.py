#!/usr/bin/env python3
"""
LinkedIn Party Planner - Startup Script
"""

import sys
import os

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import selenium
        import webdriver_manager
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_chrome():
    """Check if Chrome browser is available"""
    import subprocess
    try:
        # Try to find Chrome on different platforms
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",    # Windows
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", # Windows 32-bit
            "/usr/bin/google-chrome",  # Linux
            "/usr/bin/chromium-browser"  # Linux Chromium
        ]
        
        for path in chrome_paths:
            if os.path.exists(path):
                print("✅ Chrome browser found")
                return True
        
        # Try using 'which' command
        result = subprocess.run(['which', 'google-chrome'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Chrome browser found")
            return True
            
        print("⚠️  Chrome browser not found in common locations")
        print("Please make sure Chrome is installed and accessible")
        return False
        
    except Exception as e:
        print(f"⚠️  Could not verify Chrome installation: {e}")
        return True  # Assume it's available

def main():
    """Main startup function"""
    print("🚀 LinkedIn Party Planner")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check Chrome
    check_chrome()
    
    print("\n📋 Starting the application...")
    print("🌐 The app will be available at: http://localhost:5000")
    print("📖 For help, see README.md")
    print("\n" + "=" * 40)
    
    # Import and run the app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 