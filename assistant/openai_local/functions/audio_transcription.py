import openai
from utils.file_handling import write_output_to_file
from terminal.components.system_messages import *
from terminal.components.assistant_output import print_transcription


def transcribe_audio(file_path):
    """
    	transcribe_audio function takes a file path as a parameter and transcribes the audio file using OpenAI's audio API. It handles file opening errors and OpenAI API exceptions, and then processes the transcribed response by stripping any leading or trailing whitespaces. It finally writes the output to a file and prints the transcription.
    """
    try:
        file = open(file_path, "rb")
    except:
        error_file_not_found(file_path)
        return

    try:
        response: str = openai.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            response_format="text",
        )
    except Exception as e:
        error_openai()
        return

    response: str = response.strip()


    write_output_to_file(response)
    print_transcription(response)
