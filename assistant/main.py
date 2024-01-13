import config
from openai_handler.text_generation import *
from openai_handler.image_generation import *
from openai_handler.audio_transcription import *
from openai_handler.audio_generation import *
from cli.interface import *
from cli.commands import *

def main():
    user_name = initiliaze(config)

    conversation_history = []

    while True:
        prompt = user_input(user_name)

        if prompt[0] == "/":
            if prompt.startswith("/imagine "):
                image_output(generate_image(prompt[9:]))
            elif prompt.startswith("/transcribe "):
                transcription_output(transcribe_audio(prompt[12:]))
            elif prompt.startswith("/text-to-speech "):
                audio_output(generate_audio(prompt[16:]))
            elif prompt == "/restart":
                conversation_history = []
            elif prompt == "/quit":
                quit(user_name)
            elif prompt == "/help":
                help()
            else:
                error()
        else:
            response, conversation_history = generate_text(prompt, conversation_history)
            assistant_output(response)

if __name__ == '__main__':
    main()
