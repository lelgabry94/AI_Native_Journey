from nicegui import ui
import os
from dotenv import load_dotenv
import asyncio
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet

load_dotenv()

@ui.page('/')
def main():
    with ui.column().classes('max-w-4xl mx-auto p-6'):
        # Header
        ui.markdown('# ✨ AuraCraft AI Content Strategist')
        ui.markdown('Generate professional social media content plans with AI')
        ui.separator()
        
        # Simple form
        with ui.card().classes('p-6 mb-4'):
            ui.markdown('## 📝 Content Settings')
            
            platform = ui.select(
                options=['Instagram Reels', 'TikTok', 'YouTube Shorts'],
                value='Instagram Reels',
                label='Platform'
            ).classes('mb-3')
            
            topic = ui.input(
                label='Topic', 
                value='AI art tutorials for beginners'
            ).classes('mb-3')
            
            posts = ui.number(
                label='Posts per week', 
                value=3, 
                min=1, 
                max=7
            ).classes('mb-3')
            
            style = ui.input(
                label='Style/Theme', 
                value='Pixel art aesthetics'
            ).classes('mb-3')
            
            format_type = ui.input(
                label='Format', 
                value='Short actionable tips'
            ).classes('mb-3')
            
            vibe = ui.input(
                label='Vibe', 
                value='Inspiring and empowering'
            ).classes('mb-3')
        
        # Results area
        results = ui.column()
        
        async def generate():
            results.clear()
            
            with results:
                ui.spinner('dots', size='lg')
                ui.markdown('Generating content...')
                
                user_input = {
                    'target_social_media_platform': platform.value,
                    'specific_niche_topic': topic.value,
                    'desired_number_of_posts_per_week': int(posts.value),
                    'mock_trend_1_style_theme': style.value,
                    'mock_trend_2_format_interaction': format_type.value,
                    'mock_trend_3_vibe_keywords': vibe.value,
                }
                
                try:
                    content = await asyncio.to_thread(generate_content_plan, user_input)
                    
                    results.clear()
                    with results:
                        ui.markdown('## ✅ Generated Content')
                        with ui.card().classes('p-4'):
                            ui.markdown(f'**Platform:** {platform.value}')
                            ui.markdown(f'**Topic:** {topic.value}')
                            ui.separator()
                            ui.code(content, language='markdown')
                        
                        ui.markdown('## 📊 Exporting...')
                        await asyncio.to_thread(
                            export_to_google_sheet,
                            parse_content_plan_text(content),
                            os.getenv("DEFAULT_GOOGLE_SHEET_ID", "1p28nWjH8CRrQIZ5vghF_189fjME00eATn6ni_gle71E"),
                            "Sheet1"
                        )
                        ui.markdown('✅ **Exported to Google Sheets!**')
                        
                except Exception as e:
                    results.clear()
                    with results:
                        ui.markdown(f'❌ Error: {e}')
        
        ui.button('🚀 Generate Content Plan', on_click=generate).classes('w-full mt-4')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8080, show=True)
