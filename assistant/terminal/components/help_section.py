def help_section():

    from utils.colors import cyan

    print("\n Available commands:")
    print(f"     {cyan('/imagine')} - Generate an image")
    print(f"     {cyan('/transcribe')} - Transcribe an audio file")
    print(f"     {cyan('/tts')} - Convert text to speech\n")
    print(f"     {cyan('/reset')} - Reset the conversation history\n")
    print(f"     {cyan('/help')} - Display the list of commands")
    print(f"     {cyan('/exit')} - Exit the program")
