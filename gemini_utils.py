import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate_content_plan(user_input: dict) -> str:
    """
    Generates a comprehensive social media content plan using Google Gemini.
    """
    
    # Check if API key is configured
    if not os.getenv("GOOGLE_API_KEY"):
        return "Error: GOOGLE_API_KEY not found in environment variables."
    
    print("\n--- Sending request to LLM for content plan (Google Gemini)... ---")
    
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Simple test prompt first
        test_prompt = f"""
Create a social media content plan for {user_input['target_social_media_platform']} about {user_input['specific_niche_topic']}.
Generate {user_input['desired_number_of_posts_per_week']} post ideas.

For each post, include:
- Day/Date Suggestion
- Platform  
- Post Type
- Core Concept/Topic
- Draft Caption
- Relevant Hashtags

Format each post with --- separators.
"""
        
        # Generate content
        response = model.generate_content(test_prompt)
        
        print("--- LLM response received from Gemini. ---")
        return response.text
        
    except Exception as e:
        error_msg = f"Error generating content plan with Gemini LLM: {e}"
        print(error_msg)
        return f"Error: Could not generate content plan. {e}"

# Test when run directly
if __name__ == "__main__":
    print("✅ gemini_utils.py loaded successfully!")
    print("✅ generate_content_plan function available") 