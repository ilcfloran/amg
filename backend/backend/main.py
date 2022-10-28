from typing import Optional

import typer

from backend.foobar import foobar

app = typer.Typer()


@app.command()
def main(
    number: int = typer.Argument(..., help="The number to foobar"),
    capitalize: Optional[bool] = typer.Option(False, help="Capitalize the foobar"),
):
    """
    Give me a number and I'll give you foobars
    """
    if capitalize:
        print(foobar(number).capitalize())
    else:
        print(foobar(number))
