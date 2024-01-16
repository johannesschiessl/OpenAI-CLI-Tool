import json

def initialize():

    from components.utils.colors import green, red, cyan, purple
    from components.utils.find_path_to_data_file import find_path_to_data_file

    USERNAME_FILE_PATH = find_path_to_data_file("config.json")

    with open(USERNAME_FILE_PATH, "r") as file:
        config_data = json.load(file)
        version = config_data.get("version", "")
        gpt_model = config_data.get("gpt_model", "")

    print(green(f"AI-Assistant ({version})"))
    print(red(f"\nModel: {purple(gpt_model)}\n"))

    print(f"Type {cyan('/help')} for a list of commands.")
    print(f"Type {cyan('/exit')} to exit the program.\n")

    print(f"Type {cyan('/reset')} to reset the conversation history.\n")
