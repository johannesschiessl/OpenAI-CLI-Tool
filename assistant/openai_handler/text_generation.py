from openai import OpenAI
import datetime
import json

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def generate_system_prompt():

    file_path = "data/config.json"

    with open(file_path, "r") as file:
        file_data = json.load(file)
        user_name = file_data.get("username", "")

    return f"You are a helpful assistant, based on the GPT-3.5 Turbo architecture, a large language model trained by OpenAI. Answer briefly and accurately. Current User's name: {user_name} - Knowledge cutoff: 2022-01 - Current date: {get_current_date()}"

def manage_context(new_prompt, conversation_history):
    messages = []

    if not messages:
        system_message = generate_system_prompt()
        messages.append({"role": "system", "content": system_message})

    if conversation_history is not None:
        messages.extend(conversation_history)

    return messages

def generate_text(prompt, conversation_history):
    client = OpenAI()

    with open("data/config.json", "r") as file:
        model_data = json.load(file)
        model = model_data.get("model", "")
    conversation_history.append({"role": "user", "content": prompt})
    messages = manage_context(prompt, conversation_history)

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    chatbot_response = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": chatbot_response})

    return chatbot_response, conversation_history
