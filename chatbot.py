"""DecodeLabs AI Intern Chatbot -- rule-based CLI conversation agent.

Usage:
    python chatbot.py

Type 'exit', 'quit', 'q', or 'bye bye' to stop. Press Ctrl+C to quit.
"""

import sys

WELCOME = """====================================
   DecodeLabs AI Intern Chatbot
====================================
   Type 'help' to see what I can do.
   Type 'exit' to quit.
===================================="""

FAREWELL = "Thanks for chatting with the DecodeLabs Chatbot. Goodbye!"


def get_response(user_input: str) -> str:
    """Match sanitized input to a response using if-else logic."""
    if user_input in ("hello", "hi", "hey"):
        return "Hello! I'm the DecodeLabs chatbot. How can I help you today?"

    elif user_input in ("bye", "goodbye", "see you"):
        return "Goodbye! Feel free to come back anytime."

    elif user_input in ("who are you", "your name", "what are you"):
        return "I'm the DecodeLabs AI Intern chatbot, built as part of an internship project to demonstrate clean Python and rule-based conversation design."

    elif user_input in ("help", "what can you do", "commands"):
        return "I can greet you and tell you about DecodeLabs. Try 'hello' or 'what is decodelabs'."

    elif user_input in ("thanks", "thank you"):
        return "You're welcome!"

    elif user_input in ("how are you", "are you okay"):
        return "I'm running at full capacity -- no crashes, no complaints!"

    elif user_input in ("what is decodelabs", "tell me about decodelabs"):
        return "DecodeLabs is a tech company focused on AI, data, and software engineering -- helping businesses build intelligent, scalable solutions."

    else:
        return "I'm not sure how to respond to that. Type 'help' to see what I can do."


def main() -> None:
    """Run the chatbot input loop."""
    print(WELCOME)

    try:
        while True:
            raw = input("\nYou: ")
            clean = raw.strip().lower()

            if not clean:
                continue

            if clean in ("exit", "quit", "q", "bye bye"):
                print(f"\nBot: {FAREWELL}")
                break

            response = get_response(clean)
            print(f"Bot: {response}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n\nBot: {FAREWELL}")
        sys.exit(0)


if __name__ == "__main__":
    main()
