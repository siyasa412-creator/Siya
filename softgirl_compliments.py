import random

compliments = [
    "You’re glowing today ✨",
    "Your soft-girl vibe is unmatched 💗",
    "Your creativity is so beautiful 🌸",
    "You make everything around you feel softer 🎀",
    "Your energy is gentle and magical 💕",
    "You’re doing amazing, sweet girl ✨",
    "Your aesthetic is literally goals 💗"
]

print("Soft-Girl Compliment Generator 💗✨")
print("------------------------------")
print(random.choice(compliments))

import random

# Pastel colour codes
PASTEL_PINK = "\033[38;5;218m"
PASTEL_PURPLE = "\033[38;5;183m"
PASTEL_BLUE = "\033[38;5;153m"
RESET = "\033[0m"

compliments = [
    f"{PASTEL_PINK}You’re glowing today ✨{RESET}",
    f"{PASTEL_PURPLE}Your soft-girl vibe is unmatched 💗{RESET}",
    f"{PASTEL_BLUE}Your creativity is so beautiful 🌸{RESET}",
    f"{PASTEL_PINK}You make everything around you feel softer 🎀{RESET}",
    f"{PASTEL_PURPLE}Your energy is gentle and magical 💕{RESET}",
    f"{PASTEL_BLUE}You’re doing amazing, sweet girl ✨{RESET}",
    f"{PASTEL_PINK}Your aesthetic is literally goals 💓{RESET}"
]

print(f"{PASTEL_PINK}Soft-Girl Compliment Generator 💖✨{RESET}")
print(f"{PASTEL_PURPLE}------------------------------{RESET}")
print(random.choice(compliments))


