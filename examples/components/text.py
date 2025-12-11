from reactpy import component, html
from reactpy.types import VdomChildren


@component
def Text(*children: VdomChildren):
    """Add the pico button margin to make the 
    given text line up with the button text."""

    return html.span({'id': 'pg-pages','style': 'margin-bottom: var(--spacing);'}, *children)
