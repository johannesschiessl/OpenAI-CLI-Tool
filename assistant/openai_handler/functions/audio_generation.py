from openai import OpenAI

def generate_audio(prompt):
    client = OpenAI()
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=prompt,
    )

    response.stream_to_file("data\\ai_assistant_tts.mp3")
    return "data\\ai_assistant_tts.mp3"