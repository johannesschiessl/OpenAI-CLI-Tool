import config
import openai_handler.text_generation as openai_handler
import cli.interface, cli.commands

def main():
    user_name = cli.interface.initiliaze(config)

    while True:
        prompt = cli.interface.user_input(user_name)

        if cli.commands.check_commands(prompt, user_name) is False:
            cli.interface.assistant_output(openai_handler.generate_text(user_name, prompt))

if __name__ == '__main__':
    main()
