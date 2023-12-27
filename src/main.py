import config
from openai_handler.text_generation import *
from openai_handler.image_generation import *
from cli.interface import *
from cli.commands import *

def main():
    user_name = initiliaze(config)

    while True:
        prompt = user_input(user_name)

        if cli.commands.check_commands(prompt, user_name) is False:
            cli.interface.assistant_output(openai_handler.generate_text(user_name, prompt))

if __name__ == '__main__':
    main()
