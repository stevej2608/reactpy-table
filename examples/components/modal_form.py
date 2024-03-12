from typing import Callable

from reactpy import component, event, html

from utils import EventArgs

@component
def ModalForm(open: bool, set_open: Callable[[bool], None]):

    @event(prevent_default=True)
    def close(event: EventArgs):
        set_open(False)


    return html.dialog({"open": open, "on_click": close},
        html.article(
            html.header(
                html.button({"aria-label": "Close", "rel": "prev"}, "✕"),
                html.p(html.strong("🗓️ Thank You for Registering!")),
            ),
            html.p("""
                   We're excited to have you join us for our upcoming event. 
                   Please arrive at the museum  on time to check in and 
                   get started."""),
            html.ul(html.li("Date: Saturday, April 15"), html.li("Time: 10:00am - 12:00pm")),
        ),
    )
