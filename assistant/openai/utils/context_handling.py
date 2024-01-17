from openai_handler.utils.system_prompt_handling import generate_system_prompt

def manage_context(conversation_history):
    messages = []

    if not messages:
        system_message = generate_system_prompt()
        messages.append({"role": "system", "content": system_message})

    if conversation_history is not None:
        messages.extend(conversation_history)

    return messages