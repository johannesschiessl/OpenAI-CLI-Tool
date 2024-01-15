import json

def initialize():

    from utils.colors import green, red
    from utils.find_path_to_data_file import find_path_to_data_file

    USERNAME_FILE_PATH = find_path_to_data_file("config.json")

    with open(USERNAME_FILE_PATH, "r") as file:
        config_data = json.load(file)
        version = config_data.get("version", "")
        gpt_model = config_data.get("gpt_model", "")

    print(green(f"AI-Assistant ({version})"))
    print(red(f"\nModel: {gpt_model}\n"))
