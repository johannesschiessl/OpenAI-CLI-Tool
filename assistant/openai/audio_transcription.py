from openai import OpenAI

def write_output_to_file(output, file_path):
    with open(file_path, 'w') as file:
        file.write(output)

def transcribe_audio(file_path):
    client = OpenAI()

    try:
        file = open(file_path, "rb")
    except:
        print("❌ Error: File not found. Please provide a valid file path.")
        return

    try:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            response_format="text",
        )
    except:
        print("❌ Error: An error occurred while transcribing the audio. Please try again.")
        return


    write_output_to_file(response, "data\\ai_assistant_transcription.txt")
    return response
