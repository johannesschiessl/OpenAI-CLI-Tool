import os
import json

def create_data_directory():
    if not os.path.exists("data"):
        os.makedirs("data")

class styles:
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"

    FONT_SIZE_START = "\033[6;60;]"
    FONT_SIZE_END = "\033[0m"


def initiliaze(config):
    create_data_directory()
    print(f"{styles.BOLD_START}{styles.FONT_SIZE_START}🧠 AI-Assistant (v{config.VERSION}){styles.FONT_SIZE_END}{styles.BOLD_END}")

    print("\n🚀 Type '/quit' to exit the program.")
    print("ℹ️ Type '/help' to see the list of commands.")

    username_file_path = "data/config.json"
    if os.path.exists(username_file_path) and os.path.getsize(username_file_path) > 0:
        with open(username_file_path, "r") as file:
            user_data = json.load(file)
            user_name = user_data.get("username", "")
    else:
        user_name = input("\n😀 Type in your name: ")
        with open(username_file_path, "w") as file:
            json.dump({"version": "0.1.0", "model": "gpt-3.5-turbo", "username": user_name}, file)

    print(f"\n🧠 Assistant: 👋 Hi, {user_name}! How can I help you today?")
    return user_name

def user_input(user_name):
    return input(f"😀 {user_name}: ")

def assistant_output(response):
    print(f"🧠 Assistant: {response}")

def image_output(url):
    print(f"🖼️ Image: {url}")

def transcription_output(text):
    print(f"📝 Transcription: {text}")
    print(f"📁 File: data\\ai_assistant_transcription.txt")

def audio_output(file_path):
    print(f"🎙️ Audio: {file_path}")
    print("⚠️ The audio was generated using an AI model. Not a really human voice.")

def user_file_input():
    file_path = input(f"📁 File path: ")
    return file_path
