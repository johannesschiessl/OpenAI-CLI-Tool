from openai import OpenAI
from utils.date_time_handling import *
from terminal.components.system_messages import *


def text_to_speech(prompt):
    try:
        client = OpenAI()
        response = client.Audio.create(
            model="whisper-1",
            file=open(prompt, "rb"),
        )
    except:
        error_openai()
        return None


    response.stream_to_file("data\\ai_assistant_tts.mp3")
    return "data\\ai_assistant_tts.mp3"
