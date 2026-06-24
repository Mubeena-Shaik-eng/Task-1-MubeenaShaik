import os
import requests

API_KEY = os.environ.get("GEMINI_API_KEY", "Api here")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

rules = {
    "hi": "Hello! What can I do for you?",
    "hello": "Hi there! How can I help?",
    "bye": "Goodbye! Have a great day.",
    "your name": "I'm RuleBot, your friendly assistant.",
}

def get_gemini_reply(prompt):
    try:
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(URL, json=payload, timeout=15)
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        return f"Sorry, I'm having trouble reaching my AI brain right now. ({e})"

def chatbot_response(user_input):
    text = user_input.lower().strip()
    for key in rules:
        if key in text:
            return rules[key]
    return get_gemini_reply(user_input)

print("RuleBot: Hi! I'm RuleBot. Type 'exit' or 'bye' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ["exit", "bye"]:
        print("RuleBot: Goodbye! Have a great day.")
        break
    print("RuleBot:", chatbot_response(user_input))
