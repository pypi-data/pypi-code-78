"""Format text in multiline string representations of objects."""

import textwrap


TAB_WIDTH = 2
TEXT_WIDTH = 70


def indented(text: str, tabs: int = 1) -> str:
    """Indent text of string."""
    indent = TAB_WIDTH * tabs * " "
    return textwrap.indent(text, prefix=indent)


def wrapped(text: str) -> str:
    """Wrap text of string."""
    return textwrap.fill(text, width=TEXT_WIDTH)
