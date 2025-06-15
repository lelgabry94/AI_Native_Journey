# 🧚‍♀️ Enchanted Python Script with Fairy Voice and Portal Paths (Mac friendly!)

import os

# ✨ Ask the explorer's name
name = input("What is your name, brave explorer? ✨ ")

# 🌌 Welcome message
print("\n🔮✨ Welcome, " + name + "... ✨🔮")
print("You are now entering a portal to a new realm — the realm of code!")
print("Grab your tech, ready your mind, and take your first step into the unknown...\n")

# 🎵 Fairy voice (macOS only)
try:
    os.system('say -v Princess "Welcome ' + name + ', your journey begins now"')
except Exception as e:
    print("(The fairy voice didn’t work, but the magic is still alive!)")

# 🌈 ASCII Portal Art (just characters to look like a portal)
print("""
         ✨✨✨✨✨✨✨✨
       ✨              ✨
     ✨     [  🚪  ]      ✨
       ✨              ✨
         ✨✨✨✨✨✨✨✨
""")

# 🧭 Branching Paths - Choose your destination
print("Where would you like to go next?")
print("1. Enter the Glowing Forest 🌲")
print("2. Visit the Temple of Technology 🛕")
print("3. Return to the Human World 🏠")

choice = input("Type 1, 2, or 3 and press Enter: ")

if choice == "1":
    print("\nYou wander into the Glowing Forest, where bugs are friendly and code grows on trees...")
elif choice == "2":
    print("\nYou arrive at the Temple of Technology, guided by ancient AIs whispering algorithms...")
elif choice == "3":
    print("\nYou return to the Human World, but something about you has changed... you now speak Python!")
else:
    print("\nThe portal flickers... unsure of your path. Try again, brave explorer.")
