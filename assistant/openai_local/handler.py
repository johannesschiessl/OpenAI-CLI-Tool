import openai_local

from openai import OpenAI
import json

from openai_local.utils.context_handling import manage_context
from utils.file_handling import find_path_to_data_file
from terminal.components.system_messages import *
from terminal.components.assistant_output import *


def run(prompt, conversation_history):
    try:
        with open(find_path_to_data_file("config.json"), "r") as file:
            model_data: dict = json.load(file)
            model: str = model_data.get("model", "")
        conversation_history.append({"role": "user", "content": prompt})
        messages: dict = manage_context(conversation_history)
    except Exception as e:
        error_unknown()
        return conversation_history
        
    try:
        client = OpenAI()

        response: str = ""

        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        print_newline()

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print_assistant_output(chunk.choices[0].delta.content)
                response += chunk.choices[0].delta.content

        print_newline()

    except Exception as e:
        error_openai()
        print(e)
        return conversation_history


    conversation_history.append({"role": "assistant", "content": response})

    return conversation_history
