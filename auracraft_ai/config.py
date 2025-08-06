"""
AuraCraft AI Configuration
Customize your content generation settings here
"""

# User Input Templates - Easy to customize
USER_INPUT_TEMPLATES = {
    "ai_art_tutorials": {
        "target_social_media_platform": "Instagram Reels",
        "specific_niche_topic": "AI art tutorials for beginners",
        "desired_number_of_posts_per_week": 3,
        "mock_trend_1_style_theme": "Pixel art aesthetics",
        "mock_trend_2_format_interaction": "Short, actionable tips",
        "mock_trend_3_vibe_keywords": "Inspiring and empowering",
    },
    "fitness_motivation": {
        "target_social_media_platform": "TikTok",
        "specific_niche_topic": "Home workout routines",
        "desired_number_of_posts_per_week": 5,
        "mock_trend_1_style_theme": "High-energy music",
        "mock_trend_2_format_interaction": "Quick demonstrations",
        "mock_trend_3_vibe_keywords": "Motivational and energetic",
    },
    "cooking_tips": {
        "target_social_media_platform": "YouTube Shorts",
        "specific_niche_topic": "Quick healthy meals",
        "desired_number_of_posts_per_week": 4,
        "mock_trend_1_style_theme": "Minimalist kitchen aesthetic",
        "mock_trend_2_format_interaction": "Step-by-step process",
        "mock_trend_3_vibe_keywords": "Fresh and appetizing",
    }
}

# Google Sheet Configuration
GOOGLE_SHEET_CONFIG = {
    "spreadsheet_id": "1p28nWjH8CRrQIZ5vghF_189fjME00eATn6ni_gle71E",
    "sheet_name": "Sheet1"
}

# Export Settings
EXPORT_SETTINGS = {
    "create_csv": True,
    "create_json": True,
    "include_timestamp": True,
    "max_caption_length": 150  # For preview display
}

