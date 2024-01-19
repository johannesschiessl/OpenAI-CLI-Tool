from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.style import Style

from terminal.utils.style_handling import light_gray

def print_assistant_output(output):
    print(light_gray(f"{output}"), end='')

def print_newline():
    print()


def print_code_block(code, language='python'):
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)

    custom_style = Style(bgcolor="dark_sea_green")

    panel = Panel(syntax, style=custom_style, border_style="blue")

    console = Console()
    console.print(panel)

