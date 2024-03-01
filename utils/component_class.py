from typing import Type, Any, cast
from reactpy.core.component import Component

NONE = cast(Any, None)


class ComponentClass(Component):

    def __init__(self):
        super().__init__(NONE, NONE, NONE, NONE, NONE)


def class_component(comp: Type[ComponentClass]):
    """ReactPy ComponentClass decorator

    Args:
        comp (ComponentClass): Class to be wrapped

    Usage:
    ```
        from reactpy import html, run
        from utils.component_class import class_component, ComponentClass

        @class_component
        class HelloWorld(ComponentClass):

            def render(self):
                return html.h2('Hello World!')

        run(HelloWorld)
    ```
    """

    def create_component(*argv: Any, **kwargs: Any):
        return comp(*argv, **kwargs)

    return create_component
