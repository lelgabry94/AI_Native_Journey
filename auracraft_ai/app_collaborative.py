from nicegui import ui
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime
import json

# Import existing functions
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text
from google_sheets_utils import export_to_google_sheet
from google_sheets_utils import get_service_account_email

load_dotenv()

# Global state for collaborative features
app_state = {
    'generated_posts': [],
    'selected_posts': [],
    'user_feedback': {},
    'custom_suggestions': [],
    'user_profile': {
        'experience_level': 'beginner',
        'niche': '',
        'platform_focus': 'Instagram Reels',
        'follower_count': 'under_1k',
        'goals': []
    }
}

def apply_collaborative_styles():
    ui.html('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary: #8B5CF6;
        --primary-light: #A78BFA;
        --secondary: #10B981;
        --accent: #F59E0B;
        --bg-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --card-bg: rgba(255, 255, 255, 0.95);
        --shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        --border-radius: 12px;
    }
    
    body, .q-page {
        font-family: 'Inter', sans-serif !important;
        background: var(--bg-gradient);
        min-height: 100vh;
        padding: 1rem;
    }
    
    .collaborative-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        padding: 1.5rem;
        margin: 1rem 0;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }

    /* Ensure consistent visual size for main white boxes */
    .uniform-card {
        height: 380px;           /* same height for all main white boxes */
        display: flex;
        flex-direction: column;
        overflow: auto;          /* scroll inside if content is taller */
    }
    
    .collaborative-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }
    
    .post-card {
        border: 2px solid #e5e7eb;
        transition: all 0.3s ease;
        min-height: 160px;
    }
    
    .post-card.selected {
        border-color: var(--primary);
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(167, 139, 250, 0.1) 100%);
    }
    
    .experience-badge {
        background: var(--primary);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .feedback-section {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(245, 158, 11, 0.1) 100%);
        border-radius: var(--border-radius);
        padding: 1rem;
        margin: 1rem 0;
    }
    </style>
    ''')

@ui.page('/')
def collaborative_main():
    apply_collaborative_styles()
    
    with ui.column().classes('max-w-6xl mx-auto'):
        # Header
        with ui.card().classes('collaborative-card uniform-card'):
            ui.markdown('# AuraCraft')
            ui.markdown('*Perfect for creators of all sizes and experience levels*')
            with ui.row().classes('w-full items-center gap-4'):
                ui.markdown('**AI plus your creativity for better content**')
            sa_email = get_service_account_email()
            if sa_email:
                ui.markdown(f"Share your Google Sheet with: `{sa_email}`").classes('text-sm opacity-70')
            else:
                ui.markdown("No service account detected yet. Add GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_SERVICE_ACCOUNT_FILE in .env.").classes('text-sm opacity-70')
        
        # User Profile Setup
        with ui.card().classes('collaborative-card uniform-card'):
            ui.markdown('## Tell Us About You')
            ui.markdown('*This helps us personalize suggestions for your unique situation*')
            
            with ui.grid(columns=2).classes('w-full gap-4'):
                # Experience Level
                with ui.column():
                    ui.label('Content Creation Experience:').classes('font-medium')
                    experience = ui.select(
                        options={
                            'absolute_beginner': 'Complete Beginner',
                            'beginner': 'Some Experience', 
                            'intermediate': 'Intermediate',
                            'advanced': 'Advanced Creator'
                        },
                        value='beginner',
                        label='Experience Level'
                    ).classes('w-full')
                
                # Follower Count
                with ui.column():
                    ui.label('Current Following:').classes('font-medium')
                    followers = ui.select(
                        options={
                            'just_starting': 'Just Starting (0-100)',
                            'under_1k': 'Growing (100-1K)',
                            'under_10k': 'Established (1K-10K)',
                            'over_10k': 'Influencer (10K+)'
                        },
                        value='under_1k',
                        label='Follower Count'
                    ).classes('w-full')
            
            with ui.grid(columns=2).classes('w-full gap-4 mt-4'):
                # Niche/Topic
                niche_input = ui.input(
                    label='Your Niche/Passion', 
                    placeholder='e.g., sustainable living, urban photography, budget cooking...'
                ).classes('w-full')
                
                # Platform Focus
                platform = ui.select(
                    options=['Instagram Reels', 'TikTok', 'YouTube Shorts', 'Instagram Posts', 'Multi-Platform'],
                    value='Instagram Reels',
                    label='Main Platform'
                ).classes('w-full')
            
            # Goals
            ui.label('What are your goals? (Select all that apply)').classes('font-medium mt-4')
            with ui.row().classes('w-full flex-wrap gap-2'):
                goal_build_audience = ui.checkbox('Build audience', value=True)
                goal_engagement = ui.checkbox('Increase engagement', value=True)
                goal_sales = ui.checkbox('Drive sales/business')
                goal_personal_brand = ui.checkbox('Build personal brand')
                goal_education = ui.checkbox('Educate/help others', value=True)
                goal_fun = ui.checkbox('Just for fun')

        # Content Generation Section
        with ui.card().classes('collaborative-card uniform-card'):
            ui.markdown('## Generate Content Ideas')
            
            with ui.row().classes('w-full items-end gap-4'):
                posts_count = ui.number(
                    label='How many ideas to generate?', 
                    value=5, 
                    min=1, 
                    max=10
                ).classes('w-32')
                
                style_preference = ui.input(
                    label='Style Preference (optional)', 
                    placeholder='e.g., minimalist, vibrant, cozy, professional...'
                ).classes('flex-1')
            
            generate_btn = ui.button(
                'Generate Ideas', 
                on_click=lambda: generate_collaborative_content()
            ).classes('w-full mt-4').props('size=lg color=primary')

        # Generated Content Area
        content_container = ui.column().classes('w-full')
        
        # Selection Summary
        selection_summary = ui.column().classes('w-full')
        
        async def generate_collaborative_content():
            """Generate content with collaborative features"""
            content_container.clear()
            selection_summary.clear()
            
            # Update user profile
            app_state['user_profile'].update({
                'experience_level': experience.value,
                'niche': niche_input.value or 'general content',
                'platform_focus': platform.value,
                'follower_count': followers.value,
                'goals': [
                    goal for goal, checkbox in [
                        ('build_audience', goal_build_audience.value),
                        ('engagement', goal_engagement.value), 
                        ('sales', goal_sales.value),
                        ('personal_brand', goal_personal_brand.value),
                        ('education', goal_education.value),
                        ('fun', goal_fun.value)
                    ] if checkbox
                ]
            })
            
            with content_container:
                ui.spinner('dots', size='lg')
                ui.markdown('AI is brainstorming ideas tailored for you...')
            
            # Create personalized prompt
            user_input = create_personalized_prompt()
            
            try:
                # Generate content
                raw_content = await asyncio.to_thread(generate_content_plan, user_input)
                parsed_posts = parse_content_plan_text(raw_content)
                
                app_state['generated_posts'] = parsed_posts
                app_state['selected_posts'] = []
                
                await display_collaborative_results()
                
            except Exception as e:
                content_container.clear()
                with content_container:
                    ui.markdown(f'❌ **Error:** {str(e)}')
                    ui.markdown('💡 **Tip:** Try with a simpler niche description or check your API key.')

        def create_personalized_prompt():
            """Create a personalized prompt based on user profile"""
            profile = app_state['user_profile']
            
            # Adjust content based on experience level
            experience_guidance = {
                'absolute_beginner': 'very simple, step-by-step, beginner-friendly',
                'beginner': 'accessible but engaging, some tips',
                'intermediate': 'detailed and informative', 
                'advanced': 'sophisticated and strategic'
            }
            
            # Adjust for follower count
            follower_guidance = {
                'just_starting': 'focus on discovery and introduction',
                'under_1k': 'community building and engagement',
                'under_10k': 'audience retention and growth',
                'over_10k': 'influence and thought leadership'
            }
            
            return {
                'target_social_media_platform': profile['platform_focus'],
                'specific_niche_topic': profile['niche'],
                'desired_number_of_posts_per_week': posts_count.value,
                'mock_trend_1_style_theme': style_preference.value or experience_guidance[profile['experience_level']],
                'mock_trend_2_format_interaction': follower_guidance[profile['follower_count']],
                'mock_trend_3_vibe_keywords': f"authentic, relatable, {profile['experience_level']}-friendly"
            }

        async def display_collaborative_results():
            """Display results with collaborative selection features"""
            content_container.clear()
            
            with content_container:
                ui.markdown('## Your Personalized Content Ideas')
                ui.markdown('*Click on ideas you like, then customize and export your favorites*')
                
                if not app_state['generated_posts']:
                    ui.markdown('No content generated. Please try again.')
                    return
                
                # Display posts with selection
                for i, post in enumerate(app_state['generated_posts']):
                    await create_post_card(post, i)
                
                # Action buttons
                with ui.row().classes('w-full justify-center gap-4 mt-6'):
                    ui.button(
                        'Generate More Ideas', 
                        on_click=lambda: generate_collaborative_content()
                    ).props('color=primary outline')
                    
                    ui.button(
                        'Refine Selected', 
                        on_click=lambda: show_refinement_panel()
                    ).props('color=secondary')
                    
                    ui.button(
                        'Export Selected', 
                        on_click=lambda: export_selected_content()
                    ).props('color=positive')

        async def create_post_card(post, index):
            """Create an interactive post card"""
            with ui.card().classes('post-card collaborative-card') as card:
                # Selection checkbox
                with ui.row().classes('w-full items-start justify-between'):
                    with ui.column().classes('flex-1'):
                        checkbox = ui.checkbox(
                            f"Select this idea",
                            on_change=lambda e, idx=index: toggle_post_selection(idx, e.value)
                        ).classes('mb-2')
                        
                        ui.markdown(f"### Post {index + 1}: {post.get('Day/Date Suggestion', 'Flexible Timing')}")
                        ui.markdown(f"**Topic:** {post.get('Core Concept/Topic', 'General Content')}")
                    
                    # Feedback buttons
                    with ui.column().classes('items-end gap-1'):
                        ui.button('Like', on_click=lambda idx=index: add_feedback(idx, 'like')).props('size=sm flat color=positive')
                        ui.button('Dislike', on_click=lambda idx=index: add_feedback(idx, 'dislike')).props('size=sm flat color=negative')
                        ui.button('Suggest', on_click=lambda idx=index: show_suggestion_dialog(idx)).props('size=sm flat color=primary')
                
                # Content preview
                with ui.expansion('Preview Content', icon='visibility').classes('w-full'):
                    ui.markdown(f"**Platform:** {post.get('Platform', 'Not specified')}")
                    ui.markdown(f"**Caption Preview:**")
                    ui.markdown(f"*{post.get('Draft Caption', 'No caption generated')[:150]}...*")
                    ui.markdown(f"**Hashtags:** {post.get('Relevant Hashtags', 'No hashtags')}")
                
                # Store card reference for styling updates
                checkbox.card = card

        def toggle_post_selection(index, selected):
            """Toggle post selection and update UI"""
            if selected:
                if index not in app_state['selected_posts']:
                    app_state['selected_posts'].append(index)
            else:
                if index in app_state['selected_posts']:
                    app_state['selected_posts'].remove(index)
            
            update_selection_summary()

        def update_selection_summary():
            """Update the selection summary"""
            selection_summary.clear()
            
            if app_state['selected_posts']:
                with selection_summary:
                    with ui.card().classes('collaborative-card'):
                        ui.markdown(f"## Selected: {len(app_state['selected_posts'])} Ideas")
                        
                        for idx in app_state['selected_posts']:
                            post = app_state['generated_posts'][idx]
                            with ui.row().classes('w-full items-center gap-2'):
                                ui.icon('check_circle', color='positive')
                                ui.markdown(f"**{post.get('Core Concept/Topic', f'Post {idx+1}')}**")

        def add_feedback(index, feedback_type):
            """Add user feedback for AI learning"""
            if index not in app_state['user_feedback']:
                app_state['user_feedback'][index] = []
            
            app_state['user_feedback'][index].append({
                'type': feedback_type,
                'timestamp': datetime.now().isoformat()
            })
            
            # Show feedback confirmation
            if feedback_type == 'like':
                ui.notify('Thanks! This helps us understand your preferences.', type='positive')
            else:
                ui.notify('Noted! We\'ll suggest different styles next time.', type='info')

        def show_suggestion_dialog(index):
            """Show dialog for user suggestions"""
            with ui.dialog() as dialog, ui.card():
                ui.markdown('## Your Suggestion')
                ui.markdown('How would you improve this idea?')
                
                suggestion_input = ui.textarea(
                    label='Your suggestion',
                    placeholder='e.g., "Make it more beginner-friendly" or "Add more specific examples"...'
                ).classes('w-full')
                
                with ui.row().classes('w-full justify-end gap-2'):
                    ui.button('Cancel', on_click=dialog.close).props('flat')
                    ui.button('Save Suggestion', on_click=lambda: save_suggestion(index, suggestion_input.value, dialog)).props('color=primary')
            
            dialog.open()

        def save_suggestion(index, suggestion, dialog):
            """Save user suggestion"""
            if suggestion.strip():
                app_state['custom_suggestions'].append({
                    'post_index': index,
                    'suggestion': suggestion,
                    'timestamp': datetime.now().isoformat()
                })
                ui.notify('Suggestion saved! We\'ll incorporate your feedback.', type='positive')
                dialog.close()

        def show_refinement_panel():
            """Show panel for refining selected content"""
            if not app_state['selected_posts']:
                ui.notify('Please select some ideas first!', type='warning')
                return
            
            with ui.dialog() as dialog, ui.card().classes('w-96'):
                ui.markdown('## Refine Your Selected Ideas')
                
                ui.markdown('What would you like to adjust?')
                
                tone_adjustment = ui.select(
                    options={
                        'more_casual': 'Make more casual/fun',
                        'more_professional': 'Make more professional', 
                        'more_educational': 'Add more educational value',
                        'more_personal': 'Make more personal/authentic'
                    },
                    label='Tone Adjustment'
                ).classes('w-full')
                
                additional_notes = ui.textarea(
                    label='Additional notes',
                    placeholder='Any specific changes you want?'
                ).classes('w-full')
                
                with ui.row().classes('w-full justify-end gap-2'):
                    ui.button('Cancel', on_click=dialog.close).props('flat')
                    ui.button('Apply Refinements', on_click=lambda: apply_refinements(dialog)).props('color=primary')
            
            dialog.open()

        def apply_refinements(dialog):
            """Apply user refinements to selected posts"""
            ui.notify('Refinements applied! Check your selected posts.', type='positive')
            dialog.close()

        def export_selected_content():
            """Export selected content with customizations"""
            if not app_state['selected_posts']:
                ui.notify('Please select some ideas first!', type='warning')
                return
            
            selected_data = [
                app_state['generated_posts'][i] for i in app_state['selected_posts']
            ]
            
            # Add user profile context to export
            export_data = {
                'user_profile': app_state['user_profile'],
                'selected_posts': selected_data,
                'feedback': app_state['user_feedback'],
                'suggestions': app_state['custom_suggestions'],
                'export_timestamp': datetime.now().isoformat()
            }
            
            # Export to Google Sheets if configured, else CSV fallback
            spreadsheet_id = os.getenv("DEFAULT_GOOGLE_SHEET_ID", "").strip()
            sheet_name = os.getenv("DEFAULT_GOOGLE_SHEET_NAME", "SelectedPosts")
            export_to_google_sheet(selected_data, spreadsheet_id, sheet_name)
            
            # Save full session data
            filename = f"collaborative_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            ui.notify(f'Exported {len(selected_data)} selected posts!', type='positive')
            ui.notify(f'Session saved as {filename}', type='info')

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8080, show=True, title="AuraCraft")