import os
import time
import random

# --- Global Variables for Quiz Tracking ---
global_score = 0
total_questions_asked = 0

# --- Prophecy Text ---
PROPHECY_LINES = [
    "Fair explorer, heed these words, for your destiny awaits!",
    "Your very screen, a tome of ancient lore,",
    "Holds the AI native secrets you must explore.",
    "With Python spells and Jupyter scrolls so grand,",
    "You'll craft the magic to save this digital land.",
    "Go forth, brave soul, and let your code take flight,",
    "For in your hands, rests the kingdom's fading light!",
    ""
]

# --- Functions for Magical Effects and Interactivity ---

def clear_screen():
    """Clears the terminal screen for a cleaner experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.05): # Increased default delay for typing
    """Simulates a typewriter effect for text."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def speak_fairy_placeholder(message):
    """Placeholder for fairy voice - now silent in the terminal."""
    pass

def conduct_quiz(quiz_title, lesson_text, questions_data):
    """
    Conducts a lesson and a quiz for the explorer.
    questions_data: A list of dictionaries, each with 'question', 'options' (list), 'answer' (index or string).
    """
    global global_score, total_questions_asked

    clear_screen()
    type_text(f"\n--- {quiz_title} ---\n", delay=0.06) # Slightly slower title
    type_text("Welcome! Prepare to learn.")
    time.sleep(1.5) # Longer pause

    # Only show lesson if lesson_text is provided
    if lesson_text:
        type_text("\n📜 Ancient scrolls reveal their wisdom...\n", delay=0.05)
        time.sleep(1) # Longer pause before lesson starts
        for line in lesson_text:
            type_text(line, delay=0.04) # Slower lesson text
            time.sleep(0.7) # Longer pause between lesson lines
        type_text("\n...The lesson is complete. Now, let us test your understanding!\n", delay=0.05)
        type_text("Let the trials begin!")
        time.sleep(2) # Longer pause before quiz starts
    else:
        type_text("Let the trials begin, brave one!", delay=0.05)
        time.sleep(2)


    current_quiz_score = 0
    num_questions = len(questions_data)
    random.shuffle(questions_data) # Shuffle questions

    for i, q_data in enumerate(questions_data):
        clear_screen()
        type_text(f"\n--- {quiz_title} - Question {i + 1} of {num_questions} ---\n", delay=0.05) # Slower question header
        type_text(f"Question: {q_data['question']}\n", delay=0.04) # Slower question text
        
        is_correct = False
        if 'options' in q_data and q_data['options']:
            for j, option in enumerate(q_data['options']):
                type_text(f"{j + 1}. {option}", delay=0.03) # Slower options
            
            while True:
                user_answer = input("\nYour choice (type the number): ").strip()
                try:
                    user_choice_index = int(user_answer) - 1
                    if 0 <= user_choice_index < len(q_data['options']):
                        if q_data['options'][user_choice_index].lower() == q_data['answer'].lower():
                            type_text("✨ Correct! Your insight glows brighter! ✨", delay=0.04)
                            is_correct = True
                        else:
                            type_text(f"Alas, that is incorrect. The true answer was: {q_data['answer']}", delay=0.04)
                        break
                    else:
                        type_text("That is not a valid option. Please choose a number from the list.", delay=0.04)
                except ValueError:
                    type_text("Please enter a number.", delay=0.04)
        else:
            user_answer = input("\nYour answer: ").strip()
            if user_answer.lower() == q_data['answer'].lower():
                type_text("✨ Correct! Your wisdom shines! ✨", delay=0.04)
                is_correct = True
            else:
                type_text(f"Alas, that is incorrect. The true answer was: {q_data['answer']}", delay=0.04)
        
        if is_correct:
            current_quiz_score += 1
        
        time.sleep(2.5) # Longer pause after showing result

    clear_screen()
    type_text(f"\n--- {quiz_title} Results ---\n", delay=0.05)
    type_text(f"You answered {current_quiz_score} out of {num_questions} questions correctly in this trial!", delay=0.05)
    global_score += current_quiz_score
    total_questions_asked += num_questions
    type_text(f"Your total journey wisdom score: {global_score} out of {total_questions_asked} questions answered correctly so far.", delay=0.05)
    
    if current_quiz_score == num_questions:
        type_text("A true master of these arcane arts!", delay=0.05)
    elif current_quiz_score > num_questions / 2:
        type_text("Your understanding grows strong!", delay=0.05)
    else:
        type_text("Fear not, every challenge is a step towards mastery.", delay=0.05)
    
    time.sleep(4) # Even longer pause before returning to main menu


# --- Quiz Data Definitions ---
# (These remain unchanged as they define the content, not the timing)

glowing_forest_lesson = [
    "Welcome to the Glowing Forest, where the fundamental magic of Python begins!",
    "Here, we learn about **Variables**: containers that hold information.",
    "Think of them as enchanted boxes. You give the box a name (e.g., 'my_magic_stone'),",
    "and then you put something inside it (e.g., a number, some text).",
    "Example: `my_magic_stone = 100` or `greeting = \"Hello, traveler!\"`",
    "We also learn about the **print()** function, which lets your code speak!",
    "Whatever you put inside its parentheses `()` will appear in the console.",
    "Example: `print(greeting)` or `print(\"The forest whispers...\")`"
]

glowing_forest_quiz = [
    {
        'question': "How do you store the number 7 in a variable named 'magic_number'?",
        'options': ["magic_number == 7", "set magic_number = 7", "magic_number = 7", "magic_number is 7"],
        'answer': "magic_number = 7"
    },
    {
        'question': "What is the correct way to display the text 'Enchanted Forest' in Python?",
        'options': ["show('Enchanted Forest')", "display('Enchanted Forest')", "print('Enchanted Forest')", "echo 'Enchanted Forest'"],
        'answer': "print('Enchanted Forest')"
    },
    {
        'question': "What will be the output of: `spell = \"abracadabra\"` then `print(spell)`?",
        'options': ["spell", "\"abracadabra\"", "abracadabra", "error"],
        'answer': "abracadabra"
    }
]

temple_technology_lesson = [
    "Step into the Temple of Technology, where machines learn to think!",
    "This is the realm of **Machine Learning (ML)**.",
    "Instead of programming every single rule, we give computers lots of data.",
    "The computer then 'learns' patterns from this data to make predictions or decisions.",
    "Imagine teaching a dragon to identify types of treasure by showing it many examples.",
    "ML is used for things like predicting weather, recommending items, or understanding speech.",
    "It's about training models, not writing explicit if-else rules for every scenario."
]

temple_technology_quiz = [
    {
        'question': "What does 'ML' commonly stand for in the realm of technology?",
        'options': ["Mystical Logic", "Machine Learning", "Magical Linguistics", "Modern Language"],
        'answer': "Machine Learning"
    },
    {
        'question': "Is Machine Learning primarily about writing explicit, step-by-step instructions for every task, or about training computers to learn patterns from data?",
        'options': ["Writing explicit instructions", "Training computers to learn from data"],
        'answer': "Training computers to learn from data"
    },
    {
        'question': "Name one real-world application where Machine Learning might be used. (e.g., predicting X, recommending Y, classifying Z)",
        'options': None,
        'answer': "predicting weather" # Example answer
    }
]

mastery_quiz_questions = [
    {
        'question': "In Python, what is a 'variable' often compared to?",
        'options': ["A talking parrot", "An enchanted box that holds information", "A shimmering portal to another realm", "A forgotten scroll"],
        'answer': "An enchanted box that holds information"
    },
    {
        'question': "Which Python function allows your code to 'speak' and display text in the terminal?",
        'options': ["input()", "speak()", "display()", "print()"],
        'answer': "print()"
    },
    {
        'question': "If you wanted to get a user's name from the keyboard, which function would you use?",
        'options': ["get_text()", "read_line()", "input()", "user_prompt()"],
        'answer': "input()"
    },
    {
        'question': "What is the primary purpose of an `if/else` statement in Python?",
        'options': [
            "To make your code rhyming",
            "To allow your script to make decisions based on conditions",
            "To draw ASCII art",
            "To store multiple lines of text"
        ],
        'answer': "To allow your script to make decisions based on conditions"
    },
    {
        'question': "When prompting an AI, what is a 'persona'?",
        'options': [
            "A magical creature from a fantasy world",
            "A specific role or character you ask the AI to adopt",
            "A special type of spell",
            "A secret password for the AI"
        ],
        'answer': "A specific role or character you ask the AI to adopt"
    },
    {
        'question': "Why is it important to explain your code to a non-technical audience?",
        'options': [
            "So they can rewrite your code themselves",
            "To build good communication skills and help others understand your AI's purpose",
            "To get more magic spells for your script",
            "It's not important, only coders need to understand"
        ],
        'answer': "To build good communication skills and help others understand your AI's purpose"
    },
    {
        'question': "What is one benefit of asking an AI for 'structured output' (e.g., bullet points, code blocks)?",
        'options': [
            "It makes the AI talk like a fairy",
            "It helps the AI generate longer responses",
            "It makes the AI's response clearer and easier to use",
            "It uses less magic"
        ],
        'answer': "It makes the AI's response clearer and easier to use"
    },
    {
        'question': "Connecting your AI creation to a 'real-world problem' helps you understand its...",
        'options': ["Color palette", "Purpose and potential impact", "Favorite animal", "Magical energy level"],
        'answer': "Purpose and potential impact"
    },
    {
        'question': "True or False: Machine Learning involves explicitly writing every single rule for a computer.",
        'options': ["True", "False"],
        'answer': "False"
    }
]


# --- Main Journey Begins! ---

clear_screen()
print("\n" * 2)
name = input("What is your name, brave explorer? ✨ ")
print("\n" * 2)

type_text(f"🔮✨ Welcome, {name}... ✨🔮", delay=0.06) # Slower welcome
time.sleep(1) # Longer pause
type_text("You are now entering a portal to a new realm — the realm of code!", delay=0.05) # Slower
time.sleep(1) # Longer pause
type_text("Grab your tech, ready your mind, and take your first step into the unknown...\n", delay=0.05) # Slower
time.sleep(2) # Even longer pause before portal

# 🌈 ASCII Portal Art
print("""
         ✨✨✨✨✨✨✨✨
       ✨              ✨
     ✨     [  🚪  ]      ✨
       ✨              ✨
         ✨✨✨✨✨✨✨✨
""")
time.sleep(2.5) # Longer pause after portal art


# --- Prophecy Unveiling ---
print("\nAs the portal shimmers, an ancient whisper fills the air, and a scroll unfurls before you...\n")
time.sleep(1.5) # Longer pause before prophecy starts

for i, line in enumerate(PROPHECY_LINES):
    if i == 0:
        type_text(line, delay=0.08) # Slower first line
        time.sleep(1.5) # Longer pause after first line
    else:
        type_text(line, delay=0.06) # Slower normal lines
        time.sleep(1) # Longer pause between lines

print("\n" * 2)
time.sleep(1.5) # Longer pause before presenting choices

# 🧭 Branching Paths - Choose your destination
while True:
    clear_screen()
    type_text("The prophecy spoken, your destiny awaits clarity.", delay=0.04) # Slower
    type_text("Where would you like to go next, wise one?", delay=0.04) # Slower
    print("\n")
    type_text("1. Enter the Glowing Forest 🌲 (Begin your coding trials - Python Basics)", delay=0.03) # Slower
    type_text("2. Visit the Temple of Technology 🛕 (Seek advanced knowledge - Intro to ML)", delay=0.03) # Slower
    type_text("3. Challenge the Grand Mastery Quiz! 🏆 (Test all your knowledge!)", delay=0.03) # Slower
    type_text("4. Return to the Human World 🏠 (Reflect on your new insights)", delay=0.03) # Slower

    choice = input("\nType 1, 2, 3, or 4 and press Enter: ").strip()

    if choice == "1":
        type_text("\nYou wander into the Glowing Forest, where bugs are friendly and code grows on trees...", delay=0.04)
        time.sleep(2.5) # Longer pause
        conduct_quiz("Glowing Forest: Python Basics", glowing_forest_lesson, glowing_forest_quiz)
        break
    elif choice == "2":
        type_text("\nYou arrive at the Temple of Technology, guided by ancient AIs whispering algorithms...", delay=0.04)
        time.sleep(2.5) # Longer pause
        conduct_quiz("Temple of Technology: Intro to Machine Learning", temple_technology_lesson, temple_technology_quiz)
        break
    elif choice == "3":
        type_text("\nYou step forward to face the Grand Mastery Quiz! May your wisdom shine brightest!", delay=0.04)
        time.sleep(2.5) # Longer pause
        conduct_quiz("Grand Mastery Quiz: All Realms", [], mastery_quiz_questions)
        break
    elif choice == "4":
        type_text("\nYou return to the Human World, but something about you has changed... you now speak Python!", delay=0.04)
        time.sleep(3.5) # Longer pause
        break
    else:
        type_text("\nThe portal flickers... unsure of your path. Try again, brave explorer.", delay=0.04)
        time.sleep(2.5)

clear_screen()
type_text("\n⚙️ The adventure continues! ⚙️", delay=0.05)
if total_questions_asked > 0:
    type_text(f"Your final wisdom score for this session: {global_score} out of {total_questions_asked} questions answered correctly.", delay=0.05)
type_text("May your code forever be true.", delay=0.05)
time.sleep(3) # Final, long pause
