# ============================================================
#  Basic Rule-Based Chatbot
#  CodeAlpha Internship – Task 4
# ============================================================

import random

# ---------- Rule definitions --------------------------------
# Each rule is a tuple: (list_of_keywords, list_of_responses)
# The bot checks if ANY keyword appears in the user's message.

RULES = [
    # Greetings
    (
        ["hello", "hi", "hey", "howdy", "hiya", "greetings", "sup"],
        ["Hi there! 👋", "Hello! How can I help you?", "Hey! Nice to see you."]
    ),
    # How are you
    (
        ["how are you", "how r u", "how do you do", "how's it going",
         "how are things", "what's up", "wassup"],
        ["I'm doing great, thanks for asking! 😊",
         "All good on my end! How about you?",
         "I'm fine, thanks! What can I do for you?"]
    ),
    # Name
    (
        ["your name", "who are you", "what are you called", "what's your name"],
        ["I'm ChatBot, your friendly assistant! 🤖",
         "You can call me ChatBot.",
         "I go by ChatBot. Nice to meet you!"]
    ),
    # Age
    (
        ["your age", "how old are you", "when were you born"],
        ["I'm ageless — just a bundle of code! 😄",
         "Age is just a number, and mine is undefined. 😅"]
    ),
    # Weather
    (
        ["weather", "temperature", "forecast", "rain", "sunny"],
        ["I can't check live weather, but I hope it's sunny where you are! ☀️",
         "Sadly I don't have weather data, but bring an umbrella just in case! 🌂"]
    ),
    # Jokes
    (
        ["joke", "funny", "make me laugh", "tell me a joke"],
        ["Why don't scientists trust atoms? Because they make up everything! 😂",
         "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 🍫",
         "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"]
    ),
    # Help
    (
        ["help", "what can you do", "features", "commands"],
        ["I can chat about greetings, jokes, your day, the time, and more. Just talk to me!",
         "Try asking: 'tell me a joke', 'what's your name', or just say hi!"]
    ),
    # Time / Date (static response since no live data)
    (
        ["time", "date", "today", "day"],
        ["I don't have a real-time clock, but your device always knows the time! ⏰",
         "Check the clock on your device — I'm not wired up to one!"]
    ),
    # Thanks
    (
        ["thank you", "thanks", "thx", "ty", "cheers"],
        ["You're welcome! 😊", "Happy to help!", "Anytime! 🤗"]
    ),
    # Feeling / mood
    (
        ["i'm sad", "i am sad", "feeling sad", "i'm bored", "bored",
         "i'm lonely", "lonely", "depressed"],
        ["Aw, I'm sorry to hear that. 😔 I'm here to chat whenever you need!",
         "Hope you feel better soon! Maybe a joke would help? 😊",
         "Everyone has tough days. You've got this! 💪"]
    ),
    (
        ["i'm happy", "i am happy", "great", "amazing", "awesome", "excited"],
        ["That's wonderful! 🎉 Keep that energy up!",
         "Love to hear it! 😄",
         "You're spreading good vibes — keep it up! ✨"]
    ),
    # Goodbye
    (
        ["bye", "goodbye", "see you", "see ya", "later", "take care", "quit", "exit"],
        ["Goodbye! Have a wonderful day! 👋",
         "See you later! Take care! 😊",
         "Bye! It was great chatting with you! 🌟"]
    ),
]

# Fallback responses when nothing matches
FALLBACKS = [
    "Hmm, I'm not sure I understand. Could you rephrase that?",
    "Interesting! Tell me more.",
    "I didn't quite catch that. Try asking something else!",
    "I'm still learning. Can you ask me something different?",
]

# Exit keywords (used to break the loop)
EXIT_KEYWORDS = {"bye", "goodbye", "see you", "see ya", "later",
                 "take care", "quit", "exit"}

# ------------------------------------------------------------


def get_response(user_input: str) -> tuple[str, bool]:
    """
    Match user input against rules and return (response, should_exit).
    Matching is case-insensitive and checks for keyword substrings.
    """
    text = user_input.lower().strip()

    for keywords, responses in RULES:
        for keyword in keywords:
            if keyword in text:
                reply = random.choice(responses)
                # Check if this is a goodbye intent
                should_exit = any(kw in text for kw in EXIT_KEYWORDS)
                return reply, should_exit

    return random.choice(FALLBACKS), False


def chat():
    """Main chat loop."""
    print("\n╔══════════════════════════════════════════════╗")
    print("║          🤖  CHATBOT  –  CodeAlpha            ║")
    print("╚══════════════════════════════════════════════╝")
    print("  Type a message and press Enter to chat.")
    print("  Type 'bye' or 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Take care! 👋\n")
            break

        if not user_input:
            print("Bot: Please say something! I'm all ears. 👂\n")
            continue

        response, should_exit = get_response(user_input)
        print(f"Bot: {response}\n")

        if should_exit:
            break

    print("  [Chat session ended]\n")


# ========================  MAIN  ============================

if __name__ == "__main__":
    chat()
