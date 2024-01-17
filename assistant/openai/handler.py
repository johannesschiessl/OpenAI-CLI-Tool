import openai
import json

from openai_handler.utils.context_handling import manage_context

from cli.components.system_messages import *


def run(prompt, conversation_history):
    try:
        with open("data/config.json", "r") as file:
            model_data = json.load(file)
            model = model_data.get("model", "")
        conversation_history.append({"role": "user", "content": prompt})
        messages = manage_context(conversation_history)
    except:
        error_unknown()
        return None, conversation_history
        
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
    except:
        error_openai()
        return None, conversation_history



    chatbot_response = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": chatbot_response})

    return chatbot_response, conversation_history
