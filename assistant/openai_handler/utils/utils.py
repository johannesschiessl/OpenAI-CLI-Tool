import datetime
import json

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def generate_system_prompt():

    file_path = "data/config.json"

    with open(file_path, "r") as file:
        file_data = json.load(file)
        user_name = file_data.get("username", "")

    return f"You are a helpful assistant. Current date: {get_current_date()}. User name: {user_name}"

def write_output_to_file(output, file_path):
    with open(file_path, 'w') as file:
        file.write(output)