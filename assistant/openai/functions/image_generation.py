from openai import OpenAI

from terminal.components.system_messages import error_openai


def generate_image(prompt):
    try:
        client = OpenAI()
        response = client.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        )
    except:
        error_openai()
        return None

    return response.data[0].url