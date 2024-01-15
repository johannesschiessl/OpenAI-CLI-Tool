from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.style import Style

def print_code_block(code, language='python'):
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)

    custom_style = Style(bgcolor="dark_sea_green")

    panel = Panel(syntax, style=custom_style, border_style="blue")

    console = Console()
    console.print(panel)
