from typing import List

from reactpy import component, html
from reactpy.core.component import Component


@component
def Text(*children: List[Component]):
    """Add the pico button margin to make the 
    given text line up with the button text."""

    return html.span({'id': 'pg-pages','style': 'margin-bottom: var(--spacing);'}, *children)
