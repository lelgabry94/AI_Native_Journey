from config import USER_INPUT_TEMPLATES
from llm_utils import generate_content_plan
from data_parser import parse_content_plan_text

# Test fitness template
fitness_input = USER_INPUT_TEMPLATES["fitness_motivation"]

print("🏋️ Testing Fitness Motivation Template:")
print(f"Platform: {fitness_input['target_social_media_platform']}")
print(f"Topic: {fitness_input['specific_niche_topic']}")
print(f"Posts/week: {fitness_input['desired_number_of_posts_per_week']}")

print("\nGenerating content...")
content = generate_content_plan(fitness_input)
parsed = parse_content_plan_text(content)

print(f"\n✅ Generated {len(parsed)} posts for {fitness_input['target_social_media_platform']}")
for i, post in enumerate(parsed, 1):
    day = post.get('Day/Date Suggestion', 'Unknown')
    topic = post.get('Core Concept/Topic', 'Unknown')[:60] + "..."
    print(f"   Post {i} ({day}): {topic}")

