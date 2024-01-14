from openai import OpenAI
from utils import *

def transcribe_audio(file_path):
    client = OpenAI()
    response = client.audio.transcriptions.create(
        model="whisper-1",
        file=open(file_path, "rb"),
        response_format="text",
    )

    write_output_to_file(response, "data\\ai_assistant_transcription.txt")
    return response
