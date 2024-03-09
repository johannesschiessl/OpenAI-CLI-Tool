from openai_local.utils.system_prompt_handling import generate_system_prompt

def manage_context(conversation_history):
    """
    Function to manage the context of a conversation.

    Parameters:
    - conversation_history: list of dictionaries containing the conversation history.

    Returns:
    - list of dictionaries representing the messages.
    """
    messages: list = []

    if not messages:
        system_message = generate_system_prompt()
        messages.append({"role": "system", "content": system_message})

    if conversation_history is not None:
        messages.extend(conversation_history)

    return messages