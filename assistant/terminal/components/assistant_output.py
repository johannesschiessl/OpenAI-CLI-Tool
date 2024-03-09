from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.style import Style

from terminal.utils.style_handling import light_gray, blue

def print_assistant_output(output):
    """
    Function to print the assistant's output in light gray without a new line.
    Parameter:
        output: the output to be printed
    Return type: None
    """
    print(light_gray(f"{output}"), end='')

def print_newline():
    """
    This function prints a new line.
    """
    print()

def print_image(url):
    """
    Function to print an image from the given URL.

    Args:
        url (str): The URL of the image to be printed.

    Returns:
        None
    """
    print_newline()
    print(blue('I have generated an image for you:'))
    print_assistant_output(url)
    print_newline()

def print_transcription(text):
    """
    Function to print the transcription of the given text.

    Args:
        text (str): The text to be transcribed.

    Returns:
        None
    """
    print_newline()
    print(blue('I have transcribed this file for you:'))
    print_assistant_output(text)
    print_newline()

def print_text_to_speech(text):
    """
    Print a text-to-speech output for the given text.

    Args:
        text (str): The text to be converted to speech.

    Returns:
        None
    """
    print_newline()
    print(blue('I have converted this text to speech for you:'))
    print_assistant_output(text)
    print_newline()


def print_code_block(code, language='python'):
    """
    Generates a code block using the provided code and language, with an optional custom style and panel.
    """
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)

    custom_style = Style(bgcolor="dark_sea_green")

    panel = Panel(syntax, style=custom_style, border_style="blue")

    console = Console()
    console.print(panel)

