import openai

from terminal.components.system_messages import error_openai
from terminal.components.assistant_output import *


def generate_image(prompt):
    try:
        response = openai.images.generate(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url",
        )
    except:
        error_openai()
        return

    print_image_url(response.data[0].url)
