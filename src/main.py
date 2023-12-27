import config
from openai_handler.text_generation import *
from openai_handler.image_generation import *
from cli.interface import *
from cli.commands import *

def main():
    user_name = initiliaze(config)

    while True:
        prompt = user_input(user_name)

        if prompt[0] == "/":
            if prompt.startswith("/imagine "):
                image_output(generate_image(prompt[9:]))
            elif prompt == "/quit":
                quit(user_name)
            elif prompt == "/help":
                help()
            else:
                error()
        else:
            assistant_output(generate_text(user_name, prompt))

if __name__ == '__main__':
    main()
