import os
import json
from datetime import datetime
from dotenv import load_dotenv
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet
from config import USER_INPUT_TEMPLATES, GOOGLE_SHEET_CONFIG, EXPORT_SETTINGS

# Load environment variables
load_dotenv()

def display_template_menu():
    """Display available content templates"""
    print("\n🎯 Choose a content template:")
    templates = list(USER_INPUT_TEMPLATES.keys())
    for i, template in enumerate(templates, 1):
        info = USER_INPUT_TEMPLATES[template]
        print(f"{i}. {template.replace('_', ' ').title()}")
        print(f"   Platform: {info['target_social_media_platform']}")
        print(f"   Topic: {info['specific_niche_topic']}")
        print(f"   Posts/week: {info['desired_number_of_posts_per_week']}")
    print(f"{len(templates) + 1}. Custom input")
    return templates

def get_user_input():
    """Get user input either from template or custom"""
    templates = display_template_menu()
    
    # For demo, use the first template (AI art tutorials)
    # In a real app, you'd get user choice
    chosen_template = "ai_art_tutorials"
    
    print(f"\n✅ Using template: {chosen_template.replace('_', ' ').title()}")
    return USER_INPUT_TEMPLATES[chosen_template]

def export_multiple_formats(structured_data, base_filename):
    """Export data in multiple formats"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    exports_created = []
    
    # CSV Export
    if EXPORT_SETTINGS["create_csv"]:
        import csv
        csv_filename = f"{base_filename}_{timestamp}.csv" if EXPORT_SETTINGS["include_timestamp"] else f"{base_filename}.csv"
        
        if structured_data:
            headers = list(structured_data[0].keys())
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(structured_data)
            exports_created.append(("CSV", csv_filename))
    
    # JSON Export
    if EXPORT_SETTINGS["create_json"]:
        json_filename = f"{base_filename}_{timestamp}.json" if EXPORT_SETTINGS["include_timestamp"] else f"{base_filename}.json"
        
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(structured_data, jsonfile, indent=2, ensure_ascii=False)
        exports_created.append(("JSON", json_filename))
    
    return exports_created

def display_summary_stats(structured_data):
    """Display summary statistics"""
    if not structured_data:
        return
    
    print(f"\n📊 Content Plan Summary:")
    print(f"   • Total posts: {len(structured_data)}")
    
    # Platform breakdown
    platforms = {}
    post_types = {}
    for post in structured_data:
        platform = post.get('Platform', 'Unknown')
        post_type = post.get('Post Type', 'Unknown')
        platforms[platform] = platforms.get(platform, 0) + 1
        post_types[post_type] = post_types.get(post_type, 0) + 1
    
    print(f"   • Platforms: {', '.join(f'{k} ({v})' for k, v in platforms.items())}")
    print(f"   • Post types: {', '.join(f'{k} ({v})' for k, v in post_types.items())}")
    
    # Hashtag analysis
    all_hashtags = []
    for post in structured_data:
        hashtags = post.get('Relevant Hashtags', '')
        if hashtags:
            # Extract hashtags
            tags = [tag.strip() for tag in hashtags.split('#') if tag.strip()]
            all_hashtags.extend(tags)
    
    if all_hashtags:
        unique_hashtags = len(set(all_hashtags))
        print(f"   • Unique hashtags: {unique_hashtags}")

def main():
    """Main AuraCraft AI execution"""
    print("🚀 AuraCraft AI: Social Media Content Strategy Generator")
    print("=" * 60)

    # STEP 1: Get User Input
    print("\n📝 Step 1: Content Configuration")
    user_input = get_user_input()
    
    print("\n--- Selected Configuration ---")
    for key, value in user_input.items():
        print(f"• {key.replace('_', ' ').title()}: {value}")
    print("=" * 40)

    # STEP 2: Generate Content Plan with AI
    print("\n🤖 Step 2: AI Content Generation")
    try:
        raw_content_plan_text = generate_content_plan(user_input)
        
        if "Error:" in raw_content_plan_text:
            print(f"❌ Generation failed: {raw_content_plan_text}")
            return

        # Show preview
        preview_length = 200
        preview = raw_content_plan_text[:preview_length]
        if len(raw_content_plan_text) > preview_length:
            preview += "..."
        print(f"�� Generated content preview: {preview}")
        print("=" * 40)

        # STEP 3: Parse and Structure Data
        print("\n📊 Step 3: Content Analysis & Parsing")
        structured_content_plan = parse_content_plan_text(raw_content_plan_text)

        if not structured_content_plan:
            print("❌ Parsing failed: No structured data found.")
            return

        print(f"✅ Successfully parsed {len(structured_content_plan)} posts")
        
        # Display structured content preview
        for i, post in enumerate(structured_content_plan, 1):
            day = post.get('Day/Date Suggestion', 'Unknown')
            topic = post.get('Core Concept/Topic', 'Unknown')
            caption = post.get('Draft Caption', '')
            
            # Truncate caption for display
            max_len = EXPORT_SETTINGS.get('max_caption_length', 100)
            if len(caption) > max_len:
                caption = caption[:max_len] + "..."
            
            print(f"   Post {i} ({day}): {topic}")
            print(f"      Caption: {caption}")

        # Display summary statistics
        display_summary_stats(structured_content_plan)
        print("=" * 40)

        # STEP 4: Export Content
        print("\n📋 Step 4: Content Export")
        
        # Multiple format export
        base_filename = "auracraft_content_plan"
        exports = export_multiple_formats(structured_content_plan, base_filename)
        
        print("💾 Local exports created:")
        for format_type, filename in exports:
            print(f"   • {format_type}: {filename}")
        
        # Google Sheets export
        try:
            export_to_google_sheet(
                structured_content_plan, 
                GOOGLE_SHEET_CONFIG["spreadsheet_id"], 
                GOOGLE_SHEET_CONFIG["sheet_name"]
            )
        except Exception as e:
            print(f"⚠️  Google Sheets export note: {e}")
        
        print("=" * 40)
        
    except Exception as e:
        print(f"❌ Error in content generation process: {e}")
        import traceback
        traceback.print_exc()
        return

    # SUCCESS MESSAGE
    print("\n🎉 SUCCESS! AuraCraft AI Content Generation Complete!")
    print(f"📅 Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 Platform: {user_input['target_social_media_platform']}")
    print(f"📝 Topic: {user_input['specific_niche_topic']}")
    print(f"📊 Posts created: {len(structured_content_plan)}")
    print("\n🚀 Your social media content strategy is ready to implement!")

if __name__ == "__main__":
    main()

