from utils.colors import red, cyan

def error_unknown():
    print(red("An unknown error occurred. Please try again."))

def error_invalid_command():
    print(red(f"Invalid command. Use {cyan('/help')} {red('to see available commands.')}"))

def error_openai():
    print(red("An error occurred with OpenAI. Please try again."))
