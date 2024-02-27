from reactpy import html
from .server_options import ServerOptions

PAGE_HEADER_TITLE = "ReactPy Dashboard"

GOOGLE_FONTS = {"rel": "preconnect", "href": "https://fonts.googleapis.com"}

GOOGLE_STATIC_FONTS = {
    "rel": "preconnect",
    "href": "https://fonts.gstatic.com",
    "crossorigin": "",
}

GOOGLE_CSS = {
    "rel": "stylesheet",
    "href": "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
}

META_VIEWPORT = {
    "name": "viewport",
    "content": "width=device-width",
    "initial-scale": 1,
}

META_COLOR = {"theme-color": "viewport", "content": "#000000"}

DEFAULT_OPTIONS = ServerOptions(
    head=[
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        html.link(GOOGLE_FONTS),
        html.link(GOOGLE_STATIC_FONTS),
        html.link(GOOGLE_CSS),
        html.title(PAGE_HEADER_TITLE),
    ]
)
