from types import FunctionType
from typing import Union, Callable, cast
from reactpy import component, html
from reactpy.types import VdomChildren, ComponentType
from reactpy.testing import DisplayFixture

PICO_CSS = {
    'rel': 'stylesheet',
    'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
    'crossorigin': 'anonymous'
}


class PicoContainer:
    """Simple wrapper for the reactpy component being tested"""

    def __init__(self, display:DisplayFixture):
        self.display = display

    async def show(self, app:Union[VdomChildren, Callable[[None], VdomChildren]]) -> None:

        if isinstance(app, FunctionType):
            children = app()
        else:
            children = cast(ComponentType, app)

        @component
        def AppContainer():
            return html._(
                html.head(
                    html.link(PICO_CSS)
                ),
                children
            )

        await self.display.show(AppContainer)
