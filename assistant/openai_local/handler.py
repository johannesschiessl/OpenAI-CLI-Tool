import openai_local

from openai import OpenAI
import json

from openai_local.utils.context_handling import manage_context
from utils.file_handling import find_path_to_data_file
from terminal.components.system_messages import *


def run(prompt, conversation_history):
    try:
        with open(find_path_to_data_file("config.json"), "r") as file:
            model_data = json.load(file)
            model = model_data.get("model", "")
        conversation_history.append({"role": "user", "content": prompt})
        messages = manage_context(conversation_history)
    except Exception as e:
        error_unknown()
        return e, conversation_history
        
    try: 
        client = OpenAI()
        response = client.chat.completions.create(
            messages=messages,
            model=model
        )
    except Exception as e:
        error_openai()
        return e, conversation_history



    chatbot_response = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": chatbot_response})

    return chatbot_response, conversation_history
