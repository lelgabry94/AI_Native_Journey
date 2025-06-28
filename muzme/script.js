// This array holds all the creative prompts for Muzme.
// Each object represents a single prompt with its text, category, and associated intentions.
// This array holds all the creative prompts for Muzme.
// Each object represents a single prompt with its text, category, and associated intentions.
const prompts = [
    // --- Visual Expression ---
    {
        text: "Express a feeling of peace using only organic shapes and soft colors. Consider using paint, collage, or even arranging natural natural objects.",
        category: "visual",
        intentions: ["peace", "calm", "grounding", "tranquility"]
    },
    {
        text: "Draw or paint a landscape that exists only in your dreams. Focus on texture and light.",
        category: "visual",
        intentions: ["dream", "imagination", "escape", "fantasy"]
    },
    {
        text: "Create a visual representation of your favorite sound. What colors, shapes, and movements would it have?",
        category: "visual",
        intentions: ["sensory", "synesthesia", "joy", "vibration"]
    },
    {
        text: "Using only lines and dots, draw the feeling of anticipation or excitement.",
        category: "visual",
        intentions: ["anticipation", "excitement", "focus", "energy"]
    },
    {
        text: "Design a creature that embodies resilience. What does it look like? What environment does it thrive in?",
        category: "visual",
        intentions: ["resilience", "strength", "growth", "endurance"]
    },
    {
        text: "Capture the essence of a fleeting memory through abstract shapes and a limited color palette.",
        category: "visual",
        intentions: ["memory", "nostalgia", "abstraction", "reflection"]
    },
    {
        text: "Illustrate a moment of quiet strength you've experienced or observed.",
        category: "visual",
        intentions: ["strength", "quiet", "inner_power", "observation"]
    },
    {
        text: "Create a visual metaphor for 'letting go'.",
        category: "visual",
        intentions: ["release", "letting_go", "freedom", "acceptance"]
    },
    {
        text: "Paint or draw the feeling of 'comfort' as if it were a physical space.",
        category: "visual",
        intentions: ["comfort", "cozy", "security", "warmth"]
    },
    {
        text: "Depict a hidden world that only you know about. What secrets does it hold?",
        category: "visual",
        intentions: ["mystery", "secret", "imagination", "wonder"]
    },

    // --- Literary Reflection ---
    {
        text: "Write a short piece (poem, journal entry, narrative fragment) about a memory that brings you comfort. Focus on the sensory details – what you saw, heard, felt, smelled.",
        category: "literary",
        intentions: ["comfort", "reflection", "nostalgia", "peace"]
    },
    {
        text: "Describe a tree that has witnessed many seasons. What stories does it hold? Write from its perspective.",
        category: "literary",
        intentions: ["reflection", "storytelling", "wisdom", "nature", "perspective"]
    },
    {
        text: "If your current mood were a weather pattern, what would it be? Describe it in detail, without explicitly naming the mood.",
        category: "literary",
        intentions: ["mood", "emotion", "metaphor", "introspection"]
    },
    {
        text: "Write a letter to your future self, offering encouragement or advice based on your current experiences.",
        category: "literary",
        intentions: ["future", "hope", "advice", "self_compassion"]
    },
    {
        text: "Craft a very short story (flash fiction) that begins with the line: 'The forgotten key lay nestled in the moss...'",
        category: "literary",
        intentions: ["storytelling", "mystery", "discovery", "imagination"]
    },
    {
        text: "Explore the concept of 'home' in a poem or short essay. It doesn't have to be a physical place.",
        category: "literary",
        intentions: ["home", "belonging", "security", "identity"]
    },
    {
        text: "Write a dialogue between two parts of yourself that are in conflict.",
        category: "literary",
        intentions: ["conflict", "inner_dialogue", "understanding", "resolution"]
    },
    {
        text: "Describe a feeling of profound gratitude. What sparked it? How does it manifest?",
        category: "literary",
        intentions: ["gratitude", "appreciation", "joy", "reflection"]
    },
    {
        text: "Write a haiku (5-7-5 syllables) about a simple, everyday moment that brought you joy.",
        category: "literary",
        intentions: ["joy", "simplicity", "mindfulness", "observation"]
    },
    {
        text: "Imagine you have a conversation with an inanimate object. What does it tell you?",
        category: "literary",
        intentions: ["imagination", "perspective", "curiosity", "play"]
    },

    // --- Movement & Sound ---
    {
        text: "What sound represents growth and unfolding? Explore it through simple body movements, humming, or creating a rhythm with everyday objects.",
        category: "movement_sound",
        intentions: ["growth", "exploration", "release", "sound", "movement"]
    },
    {
        text: "Create a simple sequence of movements that expresses lightness and freedom. Focus on how your body feels.",
        category: "movement_sound",
        intentions: ["freedom", "lightness", "joy", "body_awareness"]
    },
    {
        text: "If your current energy had a rhythm, what would it be? Express it through clapping, stomping, or a simple dance.",
        category: "movement_sound",
        intentions: ["energy", "rhythm", "expression", "release"]
    },
    {
        text: "Explore the feeling of 'grounding' through slow, deliberate movements and deep breaths. What sounds accompany this?",
        category: "movement_sound",
        intentions: ["grounding", "stability", "calm", "mindfulness"]
    },
    {
        text: "Improvise a soundscape using only your voice and body percussion that tells a story without words.",
        category: "movement_sound",
        intentions: ["storytelling", "soundscape", "improvisation", "expression"]
    },
    {
        text: "Move your body as if you are shedding something heavy. What sounds do you make as you release it?",
        category: "movement_sound",
        intentions: ["release", "shedding", "letting_go", "catharsis"]
    },
    {
        text: "Create a short melody or rhythmic pattern that represents your current state of mind.",
        category: "movement_sound",
        intentions: ["mindfulness", "emotion", "sound", "reflection"]
    },
    {
        text: "Explore the sensation of 'expansion' through movement, starting small and growing larger.",
        category: "movement_sound",
        intentions: ["growth", "expansion", "freedom", "potential"]
    },
    {
        text: "What does 'waiting' feel like in your body? Express it through stillness, subtle movements, or a repetitive sound.",
        category: "movement_sound",
        intentions: ["waiting", "patience", "stillness", "reflection"]
    },
    {
        text: "Use found objects around you to create a percussive piece that reflects the sounds of nature.",
        category: "movement_sound",
        intentions: ["nature", "sound", "creativity", "observation"]
    },

    // --- Open Exploration ---
    {
        text: "If your inner critic could speak, what would it say? Give it a voice through a doodle, a whispered sentence, or a gestural movement.",
        category: "open",
        intentions: ["self_discovery", "release", "insight", "inner_critic"]
    },
    {
        text: "Choose an object near you and give it a secret life. What does it do when no one is watching? Express this creatively.",
        category: "open",
        intentions: ["curiosity", "imagination", "play", "storytelling"]
    },
    {
        text: "What color is your current mood? Create something (anything!) using only that color and its shades.",
        category: "open",
        intentions: ["mood", "emotion", "color", "expression"]
    },
    {
        text: "If you could send a message to your past self, what would it be? Express it in any medium you choose.",
        category: "open",
        intentions: ["past", "reflection", "wisdom", "healing"]
    },
    {
        text: "Find three unrelated objects and create a story or a piece of art that connects them.",
        category: "open",
        intentions: ["connection", "creativity", "storytelling", "problem_solving"]
    },
    {
        text: "Explore the feeling of 'unfurling' or 'blossoming'. How would you express this through sound, movement, or visual art?",
        category: "open",
        intentions: ["growth", "unfurling", "blossoming", "potential"]
    },
    {
        text: "What does 'enough' feel like? Create a small piece that embodies this sensation.",
        category: "open",
        intentions: ["enough", "contentment", "gratitude", "simplicity"]
    },
    {
        text: "If you could have a conversation with your future self, what question would you ask? How would you express the answer?",
        category: "open",
        intentions: ["future", "guidance", "curiosity", "reflection"]
    },
    {
        text: "Pick a random word from a book or newspaper. Create something inspired by that word.",
        category: "open",
        intentions: ["random", "inspiration", "creativity", "play"]
    },
    {
        text: "What is a small act of kindness you can embody or reflect upon today? Express it artistically.",
        category: "open",
        intentions: ["kindness", "compassion", "gratitude", "reflection"]
    },

    // --- Breakthrough Burst ---
    {
        text: "If your current frustration had a color and texture, what would it be? Express it fiercely on paper, through loud vocalizations, or rapid, expressive movements.",
        category: "breakthrough",
        intentions: ["frustration", "release", "catharsis", "unblock", "anger"]
    },
    {
        text: "What forgotten dream calls to you? Capture its essence in a series of quick sketches, a stream-of-consciousness poem, or an improvised soundscape.",
        category: "breakthrough",
        intentions: ["discovery", "inspiration", "unblock", "curiosity", "dream"]
    },
    {
        text: "Scribble wildly on a page until you feel a shift. Then, find a hidden image within the scribbles and elaborate on it.",
        category: "breakthrough",
        intentions: ["unblock", "release", "play", "discovery"]
    },
    {
        text: "Make the loudest, most uninhibited sound you can. Then, make the quietest. Explore the space between.",
        category: "breakthrough",
        intentions: ["release", "sound", "contrast", "catharsis"]
    },
    {
        text: "Move your body without planning, letting impulse guide you. What emotions surface?",
        category: "breakthrough",
        intentions: ["impulse", "movement", "emotion", "release"]
    },
    {
        text: "Rapid-fire write for 5 minutes without stopping or editing. Don't worry about sense, just keep the pen moving.",
        category: "breakthrough",
        intentions: ["unblock", "flow", "release", "stream_of_consciousness"]
    },
    {
        text: "If your creative block was a physical barrier, how would you break through it? Act it out or draw it.",
        category: "breakthrough",
        intentions: ["block", "breakthrough", "action", "overcome"]
    },
    {
        text: "What's the most absurd idea you can think of right now? Turn it into a quick sketch or a silly poem.",
        category: "breakthrough",
        intentions: ["play", "absurdity", "unblock", "humor"]
    },
    {
        text: "Close your eyes and listen to the sounds around you. Pick one sound and create a visual or written piece inspired by its rhythm.",
        category: "breakthrough",
        intentions: ["focus", "observation", "sound", "inspiration"]
    },
    {
        text: "Tear up some old paper or fabric. Use the pieces to create something new, embracing imperfection.",
        category: "breakthrough",
        intentions: ["imperfection", "repurpose", "unblock", "play"]
    }
];


// This array holds supportive and encouraging messages to accompany the prompts.
const affirmations = [
    "Remember, process over product!",
    "Be kind to yourself in this moment.",
    "There's no right or wrong way to express.",
    "Let curiosity be your guide.",
    "Your unique expression is valid and valuable.",
    "Embrace the journey, not just the destination.",
    "Every mark, every sound, every word is a step.",
    "This is a space for exploration, not perfection."
];

/**
 * Generates a creative prompt based on category and an optional intention.
 * @param {string} category - The desired category for the prompt (e.g., 'visual', 'literary', 'movement_sound', 'open', 'breakthrough').
 * @param {string|null} [intention=null] - An optional feeling or intention to focus on.
 * @returns {object} A prompt object (text, category, intentions) or a fallback message.
 */
function generatePrompt(category, intention = null) {
    // 1. Filter prompts by category
    const categoryFilteredPrompts = prompts.filter(prompt => prompt.category === category);

    let finalFilteredPrompts = categoryFilteredPrompts;

    // 2. If an intention is provided, further filter the prompts
    if (intention && intention.trim() !== '') {
        const lowerCaseIntention = intention.toLowerCase().trim();
        finalFilteredPrompts = categoryFilteredPrompts.filter(prompt =>
            prompt.intentions.some(int => int.toLowerCase() === lowerCaseIntention)
        );
    }

    // 3. Select a random prompt from the filtered list
    if (finalFilteredPrompts.length > 0) {
        const randomIndex = Math.floor(Math.random() * finalFilteredPrompts.length);
        return finalFilteredPrompts[randomIndex];
    } else {
        // 4. Return a fallback prompt if no matches are found
        return {
            text: 'No specific prompt found for your criteria, but keep exploring!',
            category: 'fallback',
            intentions: []
        };
    }
}

// --- HTML Element References ---
// Get references to the various HTML elements we'll interact with
const categorySelect = document.getElementById('category-select');
const intentionInput = document.getElementById('intention-input');
const generateDailyBtn = document.getElementById('generate-daily-btn');
const generateBreakthroughBtn = document.getElementById('generate-breakthrough-btn');
const promptText = document.getElementById('prompt-text');
const guidanceText = document.getElementById('guidance-text');

// --- Event Listeners ---
// Add a 'click' event listener to the 'Daily Creative Invitation' button
generateDailyBtn.addEventListener('click', displayDailyPrompt);

// Add a 'click' event listener to the 'Need a Breakthrough?' button
generateBreakthroughBtn.addEventListener('click', displayBreakthroughPrompt);

// --- Functions to Display Prompts ---

/**
 * Handles the click event for the 'Daily Creative Invitation' button.
 * Generates a prompt based on selected category and optional intention, then displays it.
 */
function displayDailyPrompt() {
    // Get the selected category from the dropdown
    const selectedCategory = categorySelect.value;

    // Get the user's optional intention, trim whitespace
    const userIntention = intentionInput.value.trim();

    // Generate a prompt using our core logic
    const prompt = generatePrompt(selectedCategory, userIntention);

    // Update the HTML elements with the new prompt and a random affirmation
    promptText.textContent = prompt.text;

    // Select a random affirmation from the affirmations array
    const randomAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
    guidanceText.textContent = randomAffirmation;
}

/**
 * Handles the click event for the 'Need a Breakthrough?' button.
 * Generates a prompt specifically from the 'breakthrough' category and displays it.
 */
function displayBreakthroughPrompt() {
    // Generate a breakthrough prompt. We explicitly set the category to 'breakthrough'.
    // No specific intention is passed as these are meant to be more direct.
    const prompt = generatePrompt("breakthrough");

    // Update the HTML elements with the new prompt and a random affirmation
    promptText.textContent = prompt.text;

    // Select a random affirmation from the affirmations array
    const randomAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
    guidanceText.textContent = randomAffirmation;
}
