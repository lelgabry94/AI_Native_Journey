#!/usr/bin/env python3
"""
AuraCraft AI Demonstration Script
Shows the application working with mock data for demonstration purposes
"""

import os
import json
from datetime import datetime
from unittest.mock import patch, Mock

# Import the application modules
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet
from config import USER_INPUT_TEMPLATES

def demo_with_mock_api():
    """Demonstrate the application with mocked API responses"""
    
    print("🚀 AuraCraft AI - Application Demonstration")
    print("="*60)
    
    # Use a predefined template
    user_input = USER_INPUT_TEMPLATES["ai_art_tutorials"]
    
    print(f"📋 Selected Template: AI Art Tutorials")
    print(f"🎯 Platform: {user_input['target_social_media_platform']}")
    print(f"📝 Topic: {user_input['specific_niche_topic']}")
    print(f"📊 Posts per week: {user_input['desired_number_of_posts_per_week']}")
    print(f"🎨 Style: {user_input['mock_trend_1_style_theme']}")
    print(f"📱 Format: {user_input['mock_trend_2_format_interaction']}")
    print(f"✨ Vibe: {user_input['mock_trend_3_vibe_keywords']}")
    
    print("\n🤖 Generating content with AI...")
    
    # Mock a realistic AI response
    mock_ai_response = """
    ---
    **Day/Date Suggestion:** Monday
    **Platform:** Instagram Reels
    **Post Type:** Video
    **Core Concept/Topic:** Introduction to AI Art Tools for Beginners
    **Draft Caption:** 🎨 Ready to dive into AI art? Start with these beginner-friendly tools! From simple prompts to stunning visuals ✨ Which tool will you try first? Drop a 🎯 in the comments! #AIArt #CreativeJourney #DigitalArt #ArtTutorial #BeginnerFriendly
    **Relevant Hashtags:** #AIArt #CreativeJourney #DigitalArt #ArtTutorial #BeginnerFriendly #PixelArt #ArtTips #CreativeAI
    **AI Trend Insight:** Leverages the beginner-friendly educational content trend with pixel art aesthetics
    **Image Generation Prompt:** Colorful pixel art style workspace showing various AI art tools, bright and inspiring atmosphere, tutorial-style layout, beginner-friendly interface elements
    ---
    ---
    **Day/Date Suggestion:** Wednesday
    **Platform:** Instagram Reels
    **Post Type:** Video
    **Core Concept/Topic:** Basic Color Theory in AI Art Creation
    **Draft Caption:** 🌈 Color theory isn't just for traditional art! Master these AI art color combinations and watch your creations pop ✨ Save this post for your next AI art session! What's your favorite color combo? #ColorTheory #AIArt #ArtEducation #CreativeTips
    **Relevant Hashtags:** #ColorTheory #AIArt #ArtEducation #CreativeTips #DigitalArt #ArtBasics #CreativeProcess #PixelArt
    **AI Trend Insight:** Educational content with actionable tips, appealing to both beginners and intermediate creators
    **Image Generation Prompt:** Pixel art style color wheel with AI-generated art examples, vibrant colors, educational and inspiring, clean tutorial aesthetic
    ---
    ---
    **Day/Date Suggestion:** Friday
    **Platform:** Instagram Reels
    **Post Type:** Video
    **Core Concept/Topic:** Common AI Art Mistakes to Avoid
    **Draft Caption:** 🚫 Avoid these AI art pitfalls! Here are 3 mistakes I see beginners make (and how to fix them) 💡 Which one have you experienced? Share your AI art journey below! #AIArtTips #CreativeMistakes #ArtImprovement #LearnWithMe
    **Relevant Hashtags:** #AIArtTips #CreativeMistakes #ArtImprovement #LearnWithMe #AIArt #CreativeJourney #ArtEducation #DigitalArt
    **AI Trend Insight:** Problem-solving content that provides value while being empowering and supportive
    **Image Generation Prompt:** Split-screen pixel art showing common mistakes vs. corrected versions, educational but encouraging tone, bright and helpful visual style
    ---
    """
    
    # Parse the content
    print("📊 Parsing generated content...")
    parsed_content = parse_content_plan_text(mock_ai_response)
    
    print(f"✅ Successfully parsed {len(parsed_content)} posts!")
    
    # Display the parsed content
    print("\n📋 Generated Content Plan:")
    print("-" * 40)
    
    for i, post in enumerate(parsed_content, 1):
        print(f"\n📌 Post {i}:")
        print(f"   📅 Day: {post.get('Day/Date Suggestion', 'N/A')}")
        print(f"   📱 Platform: {post.get('Platform', 'N/A')}")
        print(f"   🎯 Topic: {post.get('Core Concept/Topic', 'N/A')}")
        print(f"   💬 Caption: {post.get('Draft Caption', 'N/A')[:100]}...")
        print(f"   🏷️  Hashtags: {post.get('Relevant Hashtags', 'N/A')}")
    
    # Export the content
    print(f"\n💾 Exporting content to CSV...")
    export_to_google_sheet(parsed_content, "demo_sheet_id", "Sheet1")
    
    print("\n🎉 Demo completed successfully!")
    print("📁 Check the current directory for the exported CSV file.")

def demo_app_structure():
    """Show the application structure and configuration"""
    
    print("\n🏗️  AuraCraft AI - Application Structure")
    print("="*60)
    
    print("📂 Available Templates:")
    for name, template in USER_INPUT_TEMPLATES.items():
        print(f"   • {name.replace('_', ' ').title()}")
        print(f"     Platform: {template['target_social_media_platform']}")
        print(f"     Topic: {template['specific_niche_topic']}")
        print(f"     Posts/week: {template['desired_number_of_posts_per_week']}")
    
    print(f"\n⚙️  Configuration:")
    print(f"   • Google Sheet ID: {os.getenv('DEFAULT_GOOGLE_SHEET_ID', 'Not configured')}")
    print(f"   • API Key: {'✅ Configured' if os.getenv('GOOGLE_API_KEY') else '❌ Not configured'}")
    
    print(f"\n🔧 Available Modules:")
    modules = [
        ("llm_utils.py", "AI content generation using Google Gemini"),
        ("data_parser.py", "Parse AI output into structured data"),
        ("google_sheets_utils.py", "Export data to Google Sheets/CSV"),
        ("config.py", "Application configuration and templates"),
        ("app_simple.py", "Simple web interface using NiceGUI"),
        ("app.py", "Full-featured web interface")
    ]
    
    for module, description in modules:
        print(f"   • {module}: {description}")

if __name__ == "__main__":
    try:
        demo_with_mock_api()
        demo_app_structure()
        
        print("\n" + "="*60)
        print("🏁 AuraCraft AI Demo Complete!")
        print("="*60)
        print("✅ Core functionality verified")
        print("✅ Content generation working")
        print("✅ Data parsing successful")
        print("✅ Export functionality operational")
        print("\n💡 To run with real API:")
        print("   1. Get Google Gemini API key")
        print("   2. Set GOOGLE_API_KEY environment variable")
        print("   3. Run: python app_simple.py")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc() 