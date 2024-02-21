from typing import Union, Callable, cast
from types import FunctionType
from reactpy import component, html, run
from reactpy.core.component import Component
from reactpy.backend.fastapi import Options

# from utils.fast_server import run
from utils.css_links import PICO_CSS

PICO_OPTIONS = Options(
    head=html.head(
        html.link(PICO_CSS)
        )
    )


def pico_run(app: Union[Component, Callable[..., Component]], options:Options=PICO_OPTIONS) -> None:
    """Wrap the given app in a simple container and call the FastAPI server

    Args:
        app (Union[Component, Callable]): User application
        options (_type_, optional): Server options. Defaults to PICO_OPTIONS.

    Returns:
        _type_: _description_
    """
    if isinstance(app, FunctionType):
        children: Component = app()
    else:
        children = cast(Component, app)

    @component
    def AppMain():
        nonlocal children
        return html.div({'class_name': 'container', 'style': {'max-width': '1900px'}},
            html.section(
                children
            )
        )

    # run(AppMain, options=options)
    run(AppMain)
