# DecodeLabs AI Intern Chatbot

A rule-based Python chatbot built with zero external dependencies -- responses are matched using if-else logic.

## How to Run

```bash
python chatbot.py
```

Type your message and press Enter. The chatbot responds instantly.

Type **exit**, **quit**, **q**, or **bye bye** to stop. Press **Ctrl+C** to quit anytime.

## Sample Conversation

```
You: hello
Bot: Hello! I'm the DecodeLabs chatbot. How can I help you today?

You: who are you
Bot: I'm the DecodeLabs AI Intern chatbot, built as part of an internship project...

You: what is decodelabs
Bot: DecodeLabs is a tech company focused on AI, data, and software engineering...

You: thanks
Bot: You're welcome!

You: exit
Bot: Thanks for chatting with the DecodeLabs Chatbot. Goodbye!
```

## What It Can Do

- Greet you
- Tell you about itself
- Explain what DecodeLabs is
- Accept thanks and status queries
- Handle empty input, mixed casing, and unknown messages gracefully

## Project Structure

```
└── chatbot.py       Entry point -- response logic via if-else chains
```

## How to Extend

Open `chatbot.py` and add a new `elif` branch to `get_response()`:

```python
def get_response(user_input: str) -> str:
    if user_input in ("hello", "hi", "hey"):
        return "Hello! ..."

    elif user_input == "tell me a fact":
        return "The first computer bug was an actual moth."

    ...
```

## Git & GitHub

```bash
git init
git add .
git commit -m "Initial commit: rule-based chatbot"
git remote add origin <your-repo-url>
git push -u origin main
```
