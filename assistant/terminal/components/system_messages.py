import json

from terminal.utils.colors import green, red, cyan, purple
from terminal.utils.find_path_to_data_file import find_path_to_data_file

def message_initialize():

    USERNAME_FILE_PATH = find_path_to_data_file("config.json")

    with open(USERNAME_FILE_PATH, "r") as file:
        config_data = json.load(file)
        version = config_data.get("version", "")
        gpt_model = config_data.get("gpt_model", "")

    print(green(f"AI-Assistant ({version})"))
    print(red(f"\nModel: {purple(gpt_model)}\n"))

    print(f"Type {cyan('/help')} for a list of commands.")
    print(f"Type {cyan('/exit')} to exit the program.\n")

    print(f"Type {cyan('/reset')} to reset the conversation history.")


def message_reset_conversation():
    print("Your conversation history has been reset.")


def message_help():

    from terminal.utils.colors import cyan

    print("\nAvailable commands:")
    print(f"     {cyan('/imagine')} - Generate an image")
    print(f"     {cyan('/transcribe')} - Transcribe an audio file")
    print(f"     {cyan('/tts')} - Convert text to speech\n")
    print(f"     {cyan('/reset')} - Reset the conversation history\n")
    print(f"     {cyan('/help')} - Display the list of commands")
    print(f"     {cyan('/exit')} - Exit the program")





# Error messages:

def error_unknown():
    print(red("\nAn unknown error occurred. Please try again."))

def error_invalid_command():
    print(red(f"\nInvalid command. Use {cyan('/help')} {red('to see available commands.')}"))

def error_openai():
    print(red("\nAn error occurred with OpenAI. Please try again."))
