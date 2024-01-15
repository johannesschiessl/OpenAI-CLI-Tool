from openai import OpenAI
import datetime

def get_current_date_time():
    current_date_time = datetime.datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d%H:%M:%S.%f")[:-3]
    return formatted_date_time

def generate_audio(prompt):
    client = OpenAI()
    try:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=open("data\\ai_assistant_transcription.txt", "rb"),
            response_format="text",
        )
    except:
        print("❌ Error: An error occurred while generating the audio. Please try again.")
        return

    response.stream_to_file("data\\ai_assistant_tts.mp3")
    return "data\\ai_assistant_tts.mp3"