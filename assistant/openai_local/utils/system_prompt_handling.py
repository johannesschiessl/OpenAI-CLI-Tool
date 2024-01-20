import json
from utils.file_handling import find_path_to_data_file
from utils.date_time_handling import get_current_date_time

def generate_system_prompt():

    file_path = find_path_to_data_file("config.json")

    with open(file_path, "r") as file:
        file_data = json.load(file)
        model = file_data.get("model", "")

    return f"You are a helpful assistant, based on the {model} architecture, a large language model trained by OpenAI. Answer briefly and accurately. Knowledge cutoff: 2022-01 - Current date: {get_current_date_time()}"
