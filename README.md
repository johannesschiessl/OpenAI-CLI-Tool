# 🧠 AI-Assistant
Welcome to AI Assistant, an intelligent companion designed to assist you with a variety of tasks using a command-line interface (CLI). Whether you have questions that need answering or require image generation, the AI Assistant is here to help.

## 🛠️ Features
### 1. Questions and Answers:
The AI Assistant is equipped to provide insightful answers to a wide range of questions. Engage in meaningful conversations and gather information effortlessly.

        😀 User: What's the diameter of the earth?
        🧠 Assistant: The diameter of the Earth is approximately 12,742 kilometers (7,918 miles).
### 2. Image Generation:
Harness the power of the AI Assistant to generate images based on your specifications. Whether you need visualizations, designs, or art, the AI Assistant has got you covered.

        😀 User: /imagine a whale in space
        🖼️ Image: link/to/image

### 3. Audio Transcription:
Utilize the AI Assistant's advanced capabilities for accurate audio transcription. Simply provide a recorded interview, meeting, or any spoken content, and receive a precise written transcription.

        😀 User: /transcribe path/to/audio/file
        📝 Transcription: Hello, World!
        📁 File: data\\ai_assistant_transcription.txt

### 4. Text-to-Speech:
Experience natural-sounding speech with the AI Assistant's text-to-speech functionality. Supply the desired text, and the AI Assistant will generate an audio file for your convenience.

        😀 User: /text-to-speech This is a test!
        🎙️ Audio: data\\ai_assistant_tts.mp3
        
## ⚙️ Installation
Follow these steps to get up and running.
It is recommended to use a virtual environment to avoid package conflicts.
Before doing any of this, navigate to the desired directory.

1. **Clone the Repository**:

       git clone https://github.com/johannesschiessl/AI-Assistant.git
2. **Navigate to the Project Directory**:

       cd AI-Assistant
3. **Install Requirements**:

       pip install -r requirements.txt
4. **Export your OpenAI API key to environmental variables**

       export OPENAI_API_KEY="your api key"
       # On Windows: setx OPENAI_API_KEY "your api key"
5. **Run the AI Assistant**
    
       python assistant/main.py
## 🐛 Issues
If you encounter any issues or have feature requests, feel free to [open an issue](https://github.com/johannesschiessl/AI-Assistant/issues/new).
