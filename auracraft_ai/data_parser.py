import re

def parse_content_plan_text(raw_text):
    """Parse raw LLM text into structured data"""
    
    parsed_posts = []
    # Split by --- delimiter
    post_blocks = [block.strip() for block in raw_text.split('---') if block.strip()]
    
    for block in post_blocks:
        post_data = {}
        lines = block.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Look for **Key:** Value pattern
            match = re.match(r'^\*\*([^:]+):\*\*\s*(.*)$', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                post_data[key] = value
            elif post_data:
                # Continue previous value
                last_key = list(post_data.keys())[-1]
                post_data[last_key] += " " + line.strip()
        
        if post_data:
            parsed_posts.append(post_data)
    
    return parsed_posts

