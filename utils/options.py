from typing import List, Any
from pydantic import BaseModel, validator, ValidationError
from reactpy.core.types import VdomDict
from reactpy import html


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


class Options(BaseModel):
    """options to be passed to the web server

    Args:
        head (List[Any]): List of page header options, css, script, title, etc
        asset_root (str): root path for assets (static, assets, etc). Default 'assets'
        asset_folder (str): path to assets folder relative to application root

    """
    head: List[Any] = []
    asset_root: str = 'assets'
    asset_folder: str = 'assets'


    @validator("head")
    @classmethod
    def validate_head(cls, value):
        vals = []
        for v in value:
            if isinstance(v, str):
                if v.endswith('.css'):
                    link = html.link({ "rel": "stylesheet", "href": v})
                    vals.append(link)
                elif v.endswith('.js'):
                    script = html.script({ "src": v})
                    vals.append(script)
                else:
                    raise ValidationError("Invalid asset extension expected [.css|.js]")

            elif isinstance(v, dict):
                if v['tagName'] in ['link', 'script', 'meta', 'title']:
                    vals.append(v)
                else:
                    raise ValidationError(f"Type {v['tagName'] } cannot be included in header")

        return vals


    def __add__(self, other):
        model = self.model_copy()
        model.head += other.head

        if other.asset_root:
            model.asset_root = other.asset_root

        if other.asset_folder:
            model.asset_folder = other.asset_folder

        return model


DEFAULT_OPTIONS = Options(
    head=[
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        html.link(GOOGLE_FONTS),
        html.link(GOOGLE_STATIC_FONTS),
        html.link(GOOGLE_CSS),
        html.title(PAGE_HEADER_TITLE),
    ]
)

# https://www.srihash.org/

BOOTSTRAP_CSS = {
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
    "integrity": "sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN",
    "crossorigin": "anonymous",
}

BOOTSTRAP_SCRIPT = {
    "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
    "integrity": "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
    "crossorigin": "anonymous",
}

BOOTSTRAP_OPTIONS = Options(
    head=[html.link(BOOTSTRAP_CSS), html.script(BOOTSTRAP_SCRIPT)]
)
