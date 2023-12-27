class styles:
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"

    FONT_SIZE_START = "\033[6;60;]"
    FONT_SIZE_END = "\033[0m"


def initiliaze(config):
    print(f"{styles.BOLD_START}{styles.FONT_SIZE_START}🧠 AI-Assistant (v{config.VERSION}){styles.FONT_SIZE_END}{styles.BOLD_END}")

    print("\n🚀 Type '/quit' to exit the program.")
    print("ℹ️ Type '/help' to see the list of commands.")

    user_name = input("\n📝 Type in your name: ")

    print(f"\n🧠 Assistant: 👋 Hi, {user_name}! How can I help you today?")
    return user_name

def user_input(user_name):
    return input(f"😀 {user_name}: ")

def assistant_output(response):
    print(f"🧠 Assistant: {response}")

def image_output(url):
    print(f"🖼️ Image: {url}")

def transcription_output(text):
    print(f"🎙️ Transcription: {text}")

def audio_output(url):
    print(f"🎙️ Audio: {url}")
