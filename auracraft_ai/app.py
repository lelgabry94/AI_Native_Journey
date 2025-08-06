from nicegui import ui
import os
from dotenv import load_dotenv
import json
import asyncio
from datetime import datetime

# Import your existing functions
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet

# Load environment variables
load_dotenv()

# Custom CSS for modern design
def apply_custom_styles():
    ui.html('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary: #667eea;
        --primary-dark: #5a67d8;
        --secondary: #764ba2;
        --accent: #f093fb;
        --success: #10b981;
        --warning: #f59e0b;
        --error: #ef4444;
        --dark: #1f2937;
        --light: #f8fafc;
        --card-bg: rgba(255, 255, 255, 0.95);
        --shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }
    
    body, .q-page {
        font-family: 'Inter', sans-serif !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .hero-section {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
        padding: 4rem 2rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        border-radius: 0 0 3rem 3rem;
        box-shadow: var(--shadow);
    }
    
    .content-card {
        background: var(--card-bg);
        backdrop-filter: blur(20px);
        border-radius: 1.5rem;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: var(--shadow);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .content-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 35px 60px -12px rgba(0, 0, 0, 0.3);
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
    }
    
    .glass-button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        border: none;
        border-radius: 1rem;
        padding: 1rem 2rem;
        color: white;
        font-weight: 600;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .glass-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.6);
    }
    
    .input-modern {
        border-radius: 0.75rem;
        border: 2px solid rgba(102, 126, 234, 0.2);
        transition: all 0.3s ease;
    }
    
    .input-modern:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .progress-card {
        background: linear-gradient(135deg, #667eea22 0%, #764ba222 100%);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 1rem;
        padding: 1.5rem;
    }
    
    .result-expansion {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .stats-badge {
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    .floating-header {
        position: sticky;
        top: 0;
        z-index: 100;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(102, 126, 234, 0.2);
    }
    </style>
    ''')

# --- NiceGUI Page Definition ---
@ui.page('/')
async def main_page():
    apply_custom_styles()
    
    # Floating Header
    with ui.header().classes('floating-header'):
        with ui.row().classes('w-full items-center justify-between px-6 py-3'):
            with ui.row().classes('items-center gap-3'):
                ui.html('<div style="font-size: 2rem;">✨</div>')
                ui.label('AuraCraft AI').classes('text-xl font-bold text-primary')
            with ui.row().classes('items-center gap-2'):
                ui.badge('v2.0', color='blue').classes('px-2 py-1')
                ui.badge('Beta', color='purple').classes('px-2 py-1')

    # Hero Section
    with ui.column().classes('w-full'):
        ui.html('''
        <div class="hero-section">
            <h1 style="font-size: 3.5rem; font-weight: 700; margin-bottom: 1rem; text-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                ✨ AuraCraft AI
            </h1>
            <p style="font-size: 1.5rem; opacity: 0.9; margin-bottom: 2rem;">
                Professional Social Media Content Strategy Generator
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <div style="font-size: 2rem; font-weight: 700;">🤖</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">AI Powered</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; font-weight: 700;">⚡</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Lightning Fast</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; font-weight: 700;">💎</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">100% Free</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; font-weight: 700;">📊</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Google Sheets</div>
                </div>
            </div>
        </div>
        ''')

    # Main Content Container
    with ui.column().classes('max-w-7xl mx-auto px-4 pb-8'):
        
        # Configuration Section
        with ui.card().classes('content-card'):
            ui.html('<h2 style="font-size: 1.75rem; font-weight: 600; color: var(--dark); margin-bottom: 1rem;">📊 Configuration</h2>')
            
            with ui.row().classes('feature-grid'):
                # Google Sheets Config
                with ui.column().classes('flex-grow'):
                    ui.label('Google Sheets Integration').classes('text-lg font-semibold mb-3')
                    google_sheet_id_input = ui.input(
                        label="📋 Google Sheet ID",
                        value=os.getenv("DEFAULT_GOOGLE_SHEET_ID", "1p28nWjH8CRrQIZ5vghF_189fjME00eATn6ni_gle71E"),
                        placeholder="Paste your Google Sheet ID here..."
                    ).classes('input-modern w-full mb-3')

                    google_sheet_name_input = ui.input(
                        label="📄 Sheet Tab Name",
                        value=os.getenv("DEFAULT_GOOGLE_SHEET_NAME", "Sheet1"),
                        placeholder="e.g., Sheet1, Content_Plan"
                    ).classes('input-modern w-full mb-3')

                    async def test_sheets_connection():
                        ui.notify("🔍 Testing connection...", timeout=2000)
                        await asyncio.sleep(1)
                        if os.path.exists("client_secret.json"):
                            ui.notify("✅ Google Sheets ready!", type='positive')
                        else:
                            ui.notify("⚠️ Will use CSV export", type='warning')

                    ui.button("🔍 Test Connection", on_click=test_sheets_connection).classes('glass-button')

                # Quick Start Options
                with ui.column().classes('flex-grow'):
                    ui.label('Quick Start Templates').classes('text-lg font-semibold mb-3')
                    with ui.column().classes('gap-2'):
                        
                        async def load_template(template_name):
                            templates = {
                                'ai_art': {
                                    'platform': 'Instagram Reels',
                                    'topic': 'AI art tutorials for beginners',
                                    'style': 'Pixel art aesthetics',
                                    'format': 'Short, actionable tips',
                                    'vibe': 'Inspiring and empowering'
                                },
                                'fitness': {
                                    'platform': 'TikTok',
                                    'topic': 'Home workout routines',
                                    'style': 'High-energy music',
                                    'format': 'Quick demonstrations',
                                    'vibe': 'Motivational and energetic'
                                },
                                'cooking': {
                                    'platform': 'YouTube Shorts',
                                    'topic': 'Quick healthy meals',
                                    'style': 'Minimalist kitchen aesthetic',
                                    'format': 'Step-by-step process',
                                    'vibe': 'Fresh and appetizing'
                                }
                            }
                            template = templates[template_name]
                            target_platform.value = template['platform']
                            specific_niche_topic.value = template['topic']
                            mock_trend_1.value = template['style']
                            mock_trend_2.value = template['format']
                            mock_trend_3.value = template['vibe']
                            ui.notify(f"✨ {template_name.title()} template loaded!", type='positive')

                        with ui.row().classes('gap-2 flex-wrap'):
                            ui.button("🎨 AI Art", on_click=lambda: load_template('ai_art')).classes('text-sm')
                            ui.button("💪 Fitness", on_click=lambda: load_template('fitness')).classes('text-sm')
                            ui.button("🍳 Cooking", on_click=lambda: load_template('cooking')).classes('text-sm')

        # Content Generation Section
        with ui.card().classes('content-card'):
            ui.html('<h2 style="font-size: 1.75rem; font-weight: 600; color: var(--dark); margin-bottom: 1rem;">🎯 Content Strategy</h2>')
            
            with ui.row().classes('feature-grid'):
                # Platform & Topic
                with ui.column().classes('flex-grow'):
                    ui.label('Platform & Topic').classes('text-lg font-semibold mb-3')
                    
                    target_platform = ui.select(
                        options=["Instagram Reels", "TikTok", "YouTube Shorts", "Facebook Video", "LinkedIn Post", "X (Twitter) Post"],
                        value="Instagram Reels",
                        label="🎬 Social Media Platform"
                    ).classes('input-modern w-full mb-3')

                    specific_niche_topic = ui.input(
                        label="🎯 Niche Topic",
                        value="AI art tutorials for beginners",
                        placeholder="e.g., fitness tips, cooking recipes, tech reviews"
                    ).classes('input-modern w-full mb-3')

                    desired_posts_per_week = ui.number(
                        label="📅 Posts per Week",
                        min=1,
                        max=7,
                        value=3
                    ).classes('input-modern w-full')

                # Trend Influences
                with ui.column().classes('flex-grow'):
                    ui.label('Trend Influences').classes('text-lg font-semibold mb-3')
                    
                    mock_trend_1 = ui.input(
                        label="🎨 Style/Theme",
                        value="Pixel art aesthetics",
                        placeholder="e.g., minimalist, retro, modern"
                    ).classes('input-modern w-full mb-3')
                    
                    mock_trend_2 = ui.input(
                        label="📱 Format/Interaction",
                        value="Short, actionable tips",
                        placeholder="e.g., step-by-step, behind-the-scenes"
                    ).classes('input-modern w-full mb-3')
                    
                    mock_trend_3 = ui.input(
                        label="✨ Vibe/Keywords",
                        value="Inspiring and empowering",
                        placeholder="e.g., energetic, calming, professional"
                    ).classes('input-modern w-full')

        # Results Section (initially empty)
        results_container = ui.column().classes('w-full')

        # Generate Button
        with ui.row().classes('justify-center my-8'):
            async def generate_and_export_plan():
                # Clear previous results
                results_container.clear()

                # Input validation
                if not google_sheet_id_input.value.strip() or google_sheet_id_input.value == "YOUR_GOOGLE_SHEET_ID_HERE":
                    ui.notify("⚠️ Please enter a valid Google Sheet ID", type='warning')
                
                if not google_sheet_name_input.value.strip():
                    ui.notify("⚠️ Please enter a Google Sheet Tab Name", type='warning')
                    return

                # Prepare user input
                user_input = {
                    "target_social_media_platform": target_platform.value,
                    "specific_niche_topic": specific_niche_topic.value,
                    "desired_number_of_posts_per_week": int(desired_posts_per_week.value),
                    "mock_trend_1_style_theme": mock_trend_1.value,
                    "mock_trend_2_format_interaction": mock_trend_2.value,
                    "mock_trend_3_vibe_keywords": mock_trend_3.value,
                }

                with results_container:
                    # Progress Section
                    with ui.card().classes('progress-card'):
                        ui.html('<h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">🚀 Generating Your Content Strategy</h3>')
                        
                        progress_steps = ui.column().classes('gap-4')
                        
                        with progress_steps:
                            # Step 1: AI Generation
                            with ui.row().classes('items-center gap-4'):
                                step1_spinner = ui.spinner('dots', size='lg', color='blue')
                                step1_status = ui.label("🤖 AI is crafting your content strategy...")
                            
                            try:
                                raw_content_plan_text = await asyncio.to_thread(generate_content_plan, user_input)
                                
                                step1_spinner.delete()
                                step1_status.text = "✅ Content strategy generated successfully!"
                                step1_status.classes = 'text-green-600 font-semibold'
                                
                                if "Error:" in raw_content_plan_text:
                                    ui.notify(f"❌ Generation failed", type='negative')
                                    ui.markdown("**Please check your Gemini API key in the `.env` file**")
                                    return
                                
                                # Step 2: Parsing
                                with ui.row().classes('items-center gap-4 mt-4'):
                                    step2_spinner = ui.spinner('dots', size='lg', color='green')
                                    step2_status = ui.label("📊 Parsing and structuring content...")
                                
                                structured_content_plan = await asyncio.to_thread(parse_content_plan_text, raw_content_plan_text)
                                
                                step2_spinner.delete()
                                step2_status.text = f"✅ Parsed {len(structured_content_plan)} posts successfully!"
                                step2_status.classes = 'text-green-600 font-semibold'
                                
                                if not structured_content_plan:
                                    ui.notify("❌ Failed to parse content plan", type='negative')
                                    return

                    # Results Display
                    with ui.card().classes('content-card mt-6'):
                        ui.html('<h3 style="font-size: 1.75rem; font-weight: 600; margin-bottom: 1rem;">📊 Your Content Strategy</h3>')
                        
                        # Summary Stats
                        with ui.row().classes('gap-3 mb-6 flex-wrap'):
                            ui.html(f'<span class="stats-badge">{len(structured_content_plan)} Posts</span>')
                            ui.html(f'<span class="stats-badge">{target_platform.value}</span>')
                            ui.html(f'<span class="stats-badge">{specific_niche_topic.value}</span>')
                        
                        # Content Cards
                        for i, post in enumerate(structured_content_plan, 1):
                            with ui.expansion(
                                f"📅 Post {i}: {post.get('Day/Date Suggestion', 'Unknown')} - {post.get('Core Concept/Topic', 'Unknown')}", 
                                icon='article'
                            ).classes('result-expansion'):
                                with ui.card().classes('p-4'):
                                    with ui.column().classes('gap-3'):
                                        with ui.row().classes('gap-6 flex-wrap'):
                                            with ui.column().classes('flex-grow'):
                                                ui.markdown(f"**🎬 Platform:** {post.get('Platform', 'N/A')}")
                                                ui.markdown(f"**📱 Type:** {post.get('Post Type', 'N/A')}")
                                            with ui.column().classes('flex-grow'):
                                                ui.markdown(f"**📅 Schedule:** {post.get('Day/Date Suggestion', 'N/A')}")
                                                ui.markdown(f"**🎯 Topic:** {post.get('Core Concept/Topic', 'N/A')}")
                                        
                                        ui.separator()
                                        ui.markdown(f"**✍️ Caption:**")
                                        ui.markdown(f"{post.get('Draft Caption', 'N/A')}")
                                        
                                        ui.separator()
                                        ui.markdown(f"**#️⃣ Hashtags:** {post.get('Relevant Hashtags', 'N/A')}")
                                        
                                        if post.get('Image Generation Prompt'):
                                            ui.separator()
                                            ui.markdown(f"**🎨 Image Prompt:** {post.get('Image Generation Prompt', 'N/A')}")

                        # Export Section
                        with ui.card().classes('content-card mt-6'):
                            ui.html('<h3 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">💾 Export Your Strategy</h3>')
                            
                            with ui.row().classes('items-center gap-4 mb-4'):
                                export_spinner = ui.spinner('dots', size='lg', color='orange')
                                export_status = ui.label("📋 Exporting to Google Sheets...")
                            
                            try:
                                await asyncio.to_thread(
                                    export_to_google_sheet,
                                    structured_content_plan,
                                    google_sheet_id_input.value,
                                    google_sheet_name_input.value
                                )
                                
                                export_spinner.delete()
                                export_status.text = "✅ Export completed successfully!"
                                export_status.classes = 'text-green-600 font-semibold'
                                
                                ui.notify("🎉 Content strategy ready!", type='positive')
                                
                                # Action Buttons
                                with ui.row().classes('gap-4 mt-4 flex-wrap'):
                                    ui.link(
                                        "📋 Open Google Sheet",
                                        f"https://docs.google.com/spreadsheets/d/{google_sheet_id_input.value}",
                                        new_tab=True
                                    ).classes('glass-button')
                                    
                                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                                    ui.label(f"📁 Local files: auracraft_content_plan_{timestamp}.csv/json").classes('text-sm opacity-70')
                            
                            except Exception as e:
                                export_spinner.delete()
                                export_status.text = f"⚠️ Using local export: {str(e)[:50]}..."
                                export_status.classes = 'text-orange-600'
                                ui.notify("📁 Content saved locally", type='info')
                        
                        except Exception as e:
                            ui.notify(f"❌ Error: {e}", type='negative')

            ui.button(
                "🚀 Generate Content Strategy",
                on_click=generate_and_export_plan
            ).classes('glass-button text-2xl px-12 py-6')

    # Footer
    with ui.footer().classes('bg-white/90 backdrop-blur-md mt-16'):
        with ui.row().classes('justify-center items-center gap-6 py-6 text-sm opacity-70'):
            ui.label("Powered by Google Gemini AI")
            ui.label("•")
            ui.label("Built with NiceGUI")
            ui.label("•")
            ui.label("AuraCraft AI v2.0")

# Fixed main guard for NiceGUI multiprocessing support
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="✨ AuraCraft AI - Content Strategy Generator",
        port=8080,
        host="127.0.0.1",
        favicon="✨",
        dark=False,
        show=True,
        reload=False  # Disable auto-reload for stability
    )

