import json

def generate_system_prompt():

    file_path = "data/config.json"

    with open(file_path, "r") as file:
        file_data = json.load(file)
        user_name = file_data.get("username", "")

    return f"You are a helpful assistant, based on the GPT-3.5 Turbo architecture, a large language model trained by OpenAI. Answer briefly and accurately. Current User's name: {user_name} - Knowledge cutoff: 2022-01 - Current date: {get_current_date()}"
