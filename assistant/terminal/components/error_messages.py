from utils.colors import red

def error_unknown():
    print(red("An unknown error occurred. Please try again."))

def error_invalid_command():
    print(red("Invalid command. Please try again."))

def error_openai():
    print(red("An error occurred with OpenAI. Please try again."))