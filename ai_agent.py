import requests
import os

with open(os.path.expanduser("~/cyber-ascension/.env")) as f:
    for line in f:
        if "OPENROUTER_API_KEY" in line:
            API_KEY = line.strip().split("=")[1]

MODEL = "meta-llama/llama-4-maverick:free"

def ask_agent(messages):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": messages
        }
    )
    data = response.json()
    
    return data["choices"][0]["message"]["content"]

def run_agent():
    print("\n=== HERMES AI AGENT — CYBER ASCENSION OS ===")
    print("Model: Hermes 3 Llama 3.1 8B")
    print("Type 'exit' to quit\n")

    messages = [
        {
            "role": "system",
            "content": "You are a cybersecurity and tech assistant helping Zion Pate build his career in infrastructure and cloud engineering. Be concise, technical, and direct."
        }
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Agent offline.")
            break
        messages.append({"role": "user", "content": user_input})
        print("\nAgent: thinking...\n")
        response = ask_agent(messages)
        messages.append({"role": "assistant", "content": response})
        print(f"Agent: {response}\n")

run_agent()
