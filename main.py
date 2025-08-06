import os
from dotenv import load_dotenv
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet

# Load environment variables from .env file
load_dotenv()

# --- Your Google Sheet Configuration ---
# Replace with the actual ID of your Google Sheet
GOOGLE_SHEET_ID = "1p28nWjH8CRrQIZ5vghF_189fjME00eATn6ni_gle71E" # <--- Your Google Sheet ID
GOOGLE_SHEET_NAME = "Sheet1" # Name of the tab/sheet within your spreadsheet

def main():
    print("AuraCraft AI: Generating Social Media Content Strategy...")

    # --- STEP 1: Simulate User Input (Mock Google Form Data) ---
    # This dictionary mimics the data we would receive from a Google Form submission.
    # You can change these values to test different scenarios!
    user_input = {
        "target_social_media_platform": "Instagram Reels", # Or "TikTok", "X/Twitter", "YouTube Shorts"
        "specific_niche_topic": "AI art tutorials for beginners", # Or "futuristic concepts", "digital painting tips"
        "desired_number_of_posts_per_week": 3,
        "mock_trend_1_style_theme": "Pixel art aesthetics", # e.g., "Vaporwave aesthetics", "Cyberpunk"
        "mock_trend_2_format_interaction": "Short, actionable tips", # e.g., "Speed painting timelapses", "Behind-the-scenes look"
        "mock_trend_3_vibe_keywords": "Inspiring and empowering", # e.g., "Upbeat synthwave", "Minimalist"
    }

    print("\n--- User Input Received ---")
    for key, value in user_input.items():
        print(f"- {key.replace('_', ' ').title()}: {value}")
    print("---------------------------")

    # --- STEP 2: AI Trend Insights & Content Strategy (LLM) ---
    try:
        raw_content_plan_text = generate_content_plan(user_input)
        
        if "Error:" in raw_content_plan_text:
            print(f"Failed to generate content plan: {raw_content_plan_text}")
            return

        print("\n--- Raw Content Plan from LLM ---")
        print(raw_content_plan_text)
        print("---------------------------------")

        # --- STEP 3: Parse LLM Output into Structured Data ---
        print("\n--- Parsing LLM Output ---")
        structured_content_plan = parse_content_plan_text(raw_content_plan_text)

        if not structured_content_plan:
            print("Failed to parse content plan. No structured data found.")
            return

        print("\n--- Structured Content Plan ---")
        import json
        # Use json.dumps for pretty printing the list of dictionaries
        print(json.dumps(structured_content_plan, indent=2))
        print("-----------------------------")

        # --- STEP 4: Export to Google Sheet ---
        print("\n--- Exporting to Google Sheet ---")
        if GOOGLE_SHEET_ID == "YOUR_GOOGLE_SHEET_ID_HERE":
            print("ERROR: Please replace 'YOUR_GOOGLE_SHEET_ID_HERE' in main.py with your actual Google Sheet ID.")
            print("To get your Google Sheet ID:")
            print("1. Create a new Google Sheet at https://docs.google.com/spreadsheets/")
            print("2. Copy the long ID from the URL (between /d/ and /edit)")
            print("3. Replace 'YOUR_GOOGLE_SHEET_ID_HERE' with that ID in main.py")
            return

        export_to_google_sheet(structured_content_plan, GOOGLE_SHEET_ID, GOOGLE_SHEET_NAME)
        print("---------------------------------")
        
    except Exception as e:
        print(f"Error in content generation process: {e}")
        return
    
    # --- Placeholder for future steps ---
    # In later steps, we'll call functions here, like:
    # image_generation_step(structured_content_plan)
    # ... and so on

    print("\n✅ AuraCraft AI content generation, parsing, and Google Sheets export complete!")

if __name__ == "__main__":
    main() 