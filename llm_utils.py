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
    
    Args:
        user_input (dict): Dictionary containing user preferences
        
    Returns:
        str: Raw text output from the LLM
    """
    
    # Check if API key is configured
    if not os.getenv("GOOGLE_API_KEY"):
        return "Error: GOOGLE_API_KEY not found in environment variables. Please check your .env file."
    
    # Build the prompt
    llm_prompt = f"""
You are an expert Social Media Content Strategist and AI Art Director. Your task is to develop a comprehensive social media content plan for one week, tailored to a specific niche and platform, incorporating provided "mock trend" insights.

**User Input:**
- **Target Platform:** {user_input['target_social_media_platform']}
- **Niche/Topic:** {user_input['specific_niche_topic']}
- **Desired Posts per Week:** {user_input['desired_number_of_posts_per_week']}
- **Mock Trend 1 (Style/Theme):** {user_input['mock_trend_1_style_theme']}
- **Mock Trend 2 (Format/Interaction):** {user_input['mock_trend_2_format_interaction']}
- **Mock Trend 3 (Vibe/Keywords):** {user_input['mock_trend_3_vibe_keywords']}

**Instructions:**
1. **Generate {user_input['desired_number_of_posts_per_week']} distinct social media post ideas for the upcoming week.**
2. **For each post, provide the following structured information:**
   * **Day/Date Suggestion:** (e.g., "Monday, July 7th" or "Day 1")
   * **Platform:** Confirm the target platform.
   * **Post Type:** (e.g., "Image Post", "Short Video Concept", "Text/Question Post", "Carousel")
   * **Core Concept/Topic:** A concise description of the post's main idea, explicitly showing how it integrates at least one of the provided "Mock Trends."
   * **Draft Caption:** An engaging, platform-appropriate caption (1-3 sentences), incorporating relevant keywords and a call to action where suitable.
   * **Relevant Hashtags:** A list of 5-10 relevant and trending-style hashtags.
   * **AI Trend Insight:** Briefly explain which mock trend(s) this post leverages and why it's a good fit for that trend.
   * **Image Generation Prompt (ONLY if Post Type is visual):** If the Post Type is "Image Post" or "Short Video Concept" (for a thumbnail/keyframe), provide a highly detailed, specific, and creative prompt for an AI image generator (like DALL-E 3). This prompt should be ready to be directly sent to an image AI and reflect the Core Concept and Mock Trends.
3. **Ensure variety** in post types and concepts across the week.
4. **Maintain a professional, creative, and engaging tone.**

**Example Output Format (for 1 post, repeat for {user_input['desired_number_of_posts_per_week']} times):**

---
**Day/Date Suggestion:** [Day, Date]
**Platform:** [Target Platform]
**Post Type:** [Image Post/Short Video Concept/Text Post/Carousel]
**Core Concept/Topic:** [Description of post, explicitly mentioning mock trends used]
**Draft Caption:** [Engaging caption]
**Relevant Hashtags:** #[hashtag1] #[hashtag2] #[hashtag3]
**AI Trend Insight:** [Explanation of trend leverage]
**Image Generation Prompt:** [Detailed DALL-E 3 prompt, if visual]
---
"""

    print("\n--- Sending request to LLM for content plan (Google Gemini)... ---")
    
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate content
        response = model.generate_content(
            llm_prompt,
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
        )
        
        print("--- LLM response received from Gemini. ---")
        return response.text
        
    except Exception as e:
        error_msg = f"Error generating content plan with Gemini LLM: {e}"
        print(error_msg)
        return f"Error: Could not generate content plan. {e}"

# Test function availability when running directly
if __name__ == "__main__":
    print("llm_utils.py - generate_content_plan function is available") 