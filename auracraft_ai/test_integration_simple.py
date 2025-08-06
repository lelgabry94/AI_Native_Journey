"""
Simple Integration Tests for AuraCraft AI
Tests core functionality with mocked dependencies
"""

import pytest
import os
import tempfile
from unittest.mock import patch, Mock
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet
from config import USER_INPUT_TEMPLATES


def test_full_workflow_mocked():
    """Test the complete workflow with mocked LLM"""
    
    # Mock LLM response
    mock_llm_response = """
    ---
    **Day/Date Suggestion:** Monday
    **Platform:** Instagram Reels
    **Post Type:** Video
    **Core Concept/Topic:** Introduction to AI art tools
    **Draft Caption:** Discover the magic of AI art! ✨ Start your creative journey today. #AIArt #CreativeTools #DigitalArt
    **Relevant Hashtags:** #AIArt #CreativeTools #DigitalArt #Tutorial #Beginner
    **AI Trend Insight:** Leverages beginner-friendly educational content trend
    **Image Generation Prompt:** Modern digital workspace with AI art tools, colorful interface, inspiring atmosphere
    ---
    ---
    **Day/Date Suggestion:** Wednesday  
    **Platform:** Instagram Reels
    **Post Type:** Video
    **Core Concept/Topic:** Basic color theory in AI art
    **Draft Caption:** Master color harmony in your AI creations! 🎨 Learn the basics that make art pop. #ColorTheory #AIArt
    **Relevant Hashtags:** #ColorTheory #AIArt #ArtBasics #CreativeTips #DigitalArt
    **AI Trend Insight:** Educational content with practical application
    **Image Generation Prompt:** Color wheel with AI-generated art examples, vibrant and educational
    ---
    """
    
    # Test data parsing
    parsed_data = parse_content_plan_text(mock_llm_response)
    
    # Verify parsing worked
    assert len(parsed_data) == 2
    assert parsed_data[0]["Day/Date Suggestion"] == "Monday"
    assert parsed_data[1]["Day/Date Suggestion"] == "Wednesday"
    assert "AI art tools" in parsed_data[0]["Core Concept/Topic"]
    assert "#AIArt" in parsed_data[0]["Relevant Hashtags"]
    
    # Test export functionality
    with tempfile.TemporaryDirectory() as temp_dir:
        original_dir = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            export_to_google_sheet(parsed_data, "test_sheet_id", "Sheet1")
            
            # Check if CSV was created
            csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
            assert len(csv_files) == 1
            
            # Verify CSV contains expected data
            with open(csv_files[0], 'r', encoding='utf-8') as f:
                content = f.read()
                assert "Monday" in content
                assert "Wednesday" in content
                assert "AI art tools" in content
        
        finally:
            os.chdir(original_dir)


def test_template_validation():
    """Test that all templates are valid"""
    for template_name, template in USER_INPUT_TEMPLATES.items():
        # Test that all required fields exist
        required_fields = [
            "target_social_media_platform",
            "specific_niche_topic",
            "desired_number_of_posts_per_week",
            "mock_trend_1_style_theme",
            "mock_trend_2_format_interaction", 
            "mock_trend_3_vibe_keywords"
        ]
        
        for field in required_fields:
            assert field in template, f"Missing {field} in {template_name}"
            assert template[field], f"Empty {field} in {template_name}"
        
        # Test that posts per week is a reasonable number
        assert 1 <= template["desired_number_of_posts_per_week"] <= 7


def test_mock_llm_integration():
    """Test LLM integration with mocking"""
    from llm_utils import generate_content_plan
    
    with patch('llm_utils.genai') as mock_genai:
        # Setup mock
        mock_model = Mock()
        mock_response = Mock()
        mock_response.text = "**Day/Date Suggestion:** Test Day\n**Platform:** Test Platform"
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        # Test with valid API key
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            user_input = USER_INPUT_TEMPLATES["ai_art_tutorials"]
            result = generate_content_plan(user_input)
            
            # Verify API was called
            mock_genai.configure.assert_called_once_with(api_key='test_key')
            mock_genai.GenerativeModel.assert_called_once_with('gemini-1.5-flash')
            
            # Verify result contains expected content
            assert "Test Day" in result
            assert "Test Platform" in result


if __name__ == "__main__":
    # Run the simple integration tests
    print("🧪 Running AuraCraft AI Integration Tests...")
    
    try:
        test_full_workflow_mocked()
        print("✅ Full workflow test - PASSED")
    except Exception as e:
        print(f"❌ Full workflow test - FAILED: {e}")
    
    try:
        test_template_validation()
        print("✅ Template validation test - PASSED")
    except Exception as e:
        print(f"❌ Template validation test - FAILED: {e}")
    
    try:
        test_mock_llm_integration()
        print("✅ Mock LLM integration test - PASSED")
    except Exception as e:
        print(f"❌ Mock LLM integration test - FAILED: {e}")
    
    print("🎉 Integration tests completed!") 