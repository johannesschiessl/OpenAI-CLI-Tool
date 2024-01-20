from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.style import Style

from terminal.utils.style_handling import light_gray, blue

def print_assistant_output(output):
    print(light_gray(f"{output}"), end='')

def print_newline():
    print()

def print_image(url):
    print_newline()
    print(blue('I have generated an image for you:'))
    print_assistant_output(url)
    print_newline()

def print_transcription(text):
    print_newline()
    print(blue('I have transcribed this file for you:'))
    print_assistant_output(text)
    print_newline()

def print_text_to_speech(text):
    print_newline()
    print(blue('I have converted this text to speech for you:'))
    print_assistant_output(text)
    print_newline()


def print_code_block(code, language='python'):
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)

    custom_style = Style(bgcolor="dark_sea_green")

    panel = Panel(syntax, style=custom_style, border_style="blue")

    console = Console()
    console.print(panel)

