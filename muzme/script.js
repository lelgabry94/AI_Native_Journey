// This array holds all the creative prompts for Muzme.
// Each object represents a single prompt with its text, category, and associated intentions.
const prompts = [
    {
        text: "Express a feeling of peace using only organic shapes and soft colors. Consider using paint, collage, or even arranging natural objects.",
        category: "visual", // Corresponds to "Visual Expression"
        intentions: ["peace", "calm", "grounding"]
    },
    {
        text: "Write a short piece (poem, journal entry, narrative fragment) about a memory that brings you comfort. Focus on the sensory details – what you saw, heard, felt, smelled.",
        category: "literary", // Corresponds to "Literary Reflection"
        intentions: ["comfort", "reflection", "nostalgia"]
    },
    {
        text: "What sound represents growth and unfolding? Explore it through simple body movements, humming, or creating a rhythm with everyday objects.",
        category: "movement_sound", // Corresponds to "Movement & Sound"
        intentions: ["growth", "exploration", "release"]
    },
    {
        text: "If your inner critic could speak, what would it say? Give it a voice through a doodle, a whispered sentence, or a gestural movement.",
        category: "open", // Corresponds to "Open Exploration"
        intentions: ["self-discovery", "release", "insight"]
    },
    {
        text: "If your current frustration had a color and texture, what would it be? Express it fiercely on paper, through loud vocalizations, or rapid, expressive movements.",
        category: "breakthrough", // Dedicated category for "Breakthrough Burst"
        intentions: ["frustration", "release", "catharsis", "unblock"]
    },
    {
        text: "What forgotten dream calls to you? Capture its essence in a series of quick sketches, a stream-of-consciousness poem, or an improvised soundscape.",
        category: "breakthrough", // Another "Breakthrough Burst" prompt
        intentions: ["discovery", "inspiration", "unblock", "curiosity"]
    },
    {
        text: "Using only lines and dots, draw the feeling of anticipation.",
        category: "visual",
        intentions: ["anticipation", "excitement", "focus"]
    },
    {
        text: "Describe a tree that has witnessed many seasons. What stories does it hold?",
        category: "literary",
        intentions: ["reflection", "storytelling", "wisdom"]
    },
    {
        text: "Create a simple sequence of movements that expresses lightness and freedom.",
        category: "movement_sound",
        intentions: ["freedom", "lightness", "joy"]
    },
    {
        text: "Choose an object near you and give it a secret life. What does it do when no one is watching?",
        category: "open",
        intentions: ["curiosity", "imagination", "play"]
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
