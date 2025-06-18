import os
import requests

SYSTEM_PROMPT = (
    "You are a highly intelligent assistant. "
    "Answer the user's questions clearly and concisely."
)

API_KEY = os.environ.get('GROQ_API_KEY')

if not API_KEY:
    raise EnvironmentError('Please set the GROQ_API_KEY environment variable.')

API_URL = "https://api.groq.com/v1/chat/completions"


def ask_groq(prompt, history=None, model="mixtral-8x7b"):
    messages = history or []
    if not messages:
        messages.append({"role": "system", "content": SYSTEM_PROMPT})
    messages.append({"role": "user", "content": prompt})
    data = {
        "model": model,
        "messages": messages,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    response = requests.post(API_URL, json=data, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()


def main():
    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("Digite 'sair' para encerrar o chat.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            break
        result = ask_groq(user_input, history)
        answer = result['choices'][0]['message']['content'].strip()
        history.append({"role": "assistant", "content": answer})
        print(f"Groq: {answer}\n")


if __name__ == "__main__":
    main()
