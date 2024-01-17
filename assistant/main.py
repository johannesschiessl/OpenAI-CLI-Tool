import config

from openai_handler.handler import run
from openai_handler.functions.image_generation import generate_image
from openai_handler.functions.text_to_speech import text_to_speech
from openai_handler.functions.audio_transcription import transcribe_audio

from cli.components.user_input import get_user_input
from cli.components.assistant_output import print_assistant_output

from cli.components.system_messages import *


def main():

    message_initialize()
    conversation_history = []

    while True:
        user_input = get_user_input()

        if user_input[0] == "/":
            if user_input.startswith("/imagine "):
                print_assistant_output(generate_image(user_input[9:]))
            elif user_input.startswith("/transcribe "):
                print_assistant_output(transcribe_audio(user_input[12:]))
            elif user_input.startswith("/tts "):
                print_assistant_output(text_to_speech(user_input[16:]))
            elif user_input == "/reset":
                conversation_history = []
                message_reset_conversation()
            elif user_input == "/exit":
                quit()
            elif user_input == "/help":
                message_help()
            else:
                error_invalid_command()
        else:
            assistant_output, conversation_history = run(user_input, conversation_history)
            print_assistant_output(assistant_output)



if __name__ == '__main__':
    main()
