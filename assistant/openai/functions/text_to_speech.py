from openai import OpenAI

from utils.date_handling import get_current_date


def text_to_speech(prompt):
    client = OpenAI()
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=prompt,
    )

    response.stream_to_file("data\\ai_assistant_tts.mp3")
    return "data\\ai_assistant_tts.mp3"
