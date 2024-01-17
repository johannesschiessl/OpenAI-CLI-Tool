import openai
from utils.file_handling import write_output_to_file
from terminal.components.system_messages import *


def transcribe_audio(file_path):

    try:
        file = open(file_path, "rb")
    except:
        error_file_not_found(file_path)
        return None

    try:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            response_format="text",
        )
    except:
        error_openai()
        return None


    write_output_to_file(response, "data\\ai_assistant_transcription.txt")
    return response
