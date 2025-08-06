import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def validate_user_input(user_input):
    """Validate user input and provide defaults for missing fields"""
    if not user_input or not isinstance(user_input, dict):
        return {
            "target_social_media_platform": "Instagram Reels",
            "specific_niche_topic": "General content",
            "desired_number_of_posts_per_week": 3,
            "mock_trend_1_style_theme": "Clean and modern",
            "mock_trend_2_format_interaction": "Engaging and interactive",
            "mock_trend_3_vibe_keywords": "Authentic and relatable"
        }
    
    # Provide defaults for missing fields
    defaults = {
        "target_social_media_platform": "Instagram Reels",
        "specific_niche_topic": "General content",
        "desired_number_of_posts_per_week": 3,
        "mock_trend_1_style_theme": "Clean and modern",
        "mock_trend_2_format_interaction": "Engaging and interactive",
        "mock_trend_3_vibe_keywords": "Authentic and relatable"
    }
    
    # Fill in missing fields with defaults
    validated_input = defaults.copy()
    validated_input.update(user_input)
    
    return validated_input

def generate_content_plan(user_input):
    """Generate social media content plan using Gemini"""
    
    if not os.getenv("GOOGLE_API_KEY"):
        return "Error: GOOGLE_API_KEY not found in environment variables."
    
    # Validate and clean input
    try:
        validated_input = validate_user_input(user_input)
    except Exception as e:
        return f"Error: Invalid input format. {str(e)}"
    
    prompt = f"""
Create a social media content plan for {validated_input['target_social_media_platform']} about {validated_input['specific_niche_topic']}.

Generate {validated_input['desired_number_of_posts_per_week']} post ideas incorporating these trends:
- Style: {validated_input['mock_trend_1_style_theme']}
- Format: {validated_input['mock_trend_2_format_interaction']}  
- Vibe: {validated_input['mock_trend_3_vibe_keywords']}

For each post, include:
---
**Day/Date Suggestion:** [Day]
**Platform:** {validated_input['target_social_media_platform']}
**Post Type:** [Image Post/Video/Text]
**Core Concept/Topic:** [Description]
**Draft Caption:** [Engaging caption with call to action]
**Relevant Hashtags:** [5-8 hashtags]
**AI Trend Insight:** [Which trends this leverages]
**Image Generation Prompt:** [Detailed visual prompt if needed]
---
"""
    
    print("\n--- Sending request to LLM for content plan (Google Gemini)... ---")
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        print("--- LLM response received from Gemini. ---")
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: Could not generate content plan. {e}"

