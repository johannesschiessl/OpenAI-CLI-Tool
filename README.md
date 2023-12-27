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
## ⚙️ Installation
Follow these steps to get up and running.
Before doing any of this, navigate to the desired directory.

1. **Clone the Repository**:

       git clone https://github.com/johannesschiessl/AI-Assistant.git
2. **Navigate to the Project Directory**:

       cd AI-Assistant
3. **Install Requirements**:
   - (optional) We recommend using a virtual environment, so if you don't have virtualenv installed, run:
    
         pip install virtualenv
   - (optional) Create and activate a virtual environment:

         virtualenv venv
         source venv/bin/activate   # On Windows: .\venv\Scripts\activate
   - Install the requirements:
   
         pip install -r requirements.txt
3. **Export your OpenAI API key to environmental variables.**

       export VARIABLE_NAME="sk-******"
       # On Windows: setx VARIABLE_NAME "sk-******"
3. **Run the AI Assistant:**:
    
       python src/main.py

## 🪄 Tips for Effective Interaction
- Be Specific: Provide clear and specific instructions for better results.
- Explore Commands: Experiment with different commands to discover the full capabilities of the AI Assistant.
- Feedback: If the AI Assistant doesn't meet your expectations, provide feedback to help improve its performance.
## 🐛 Issues
If you encounter any issues or have questions, feel free to [open an issue](https://github.com/johannesschiessl/AI-Assistant/issues/new).
