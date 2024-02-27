from typing import Union, Callable, cast
import os
import inspect
from pathlib import Path
from types import FunctionType
from reactpy import component, html
from reactpy.core.component import Component

from .css_links import PICO_CSS
from .fast_server import run
from .options import ServerOptions

PICO_OPTIONS = ServerOptions(
    head=[
        html.link(PICO_CSS)
    ]
)

def pico_run(app: Union[Component, Callable[..., Component]], options: ServerOptions | None=None):
    """Wrap the given app in a simple container and call the FastAPI server

    Args:
        app (Union[Component, Callable]): User application
        assets (List[str] | None): CSS and JS assets.

    Returns:
        _type_: _description_
    """
    if isinstance(app, FunctionType):
        children = app()
    else:
        children = cast(Component, app)

    if options is not None:
        options.asset_folder = str(Path(inspect.stack()[1].filename).parent.relative_to(os.getcwd()))
        options = PICO_OPTIONS + options
    else:
        options = PICO_OPTIONS

    @component
    def AppMain():
        return html.div({'class_name': 'container'},
            html.section(
                children
            )
        )

    run(AppMain, options=options)
