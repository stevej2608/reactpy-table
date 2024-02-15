from typing import Union, Callable, Any, List
from reactpy import component, html
from reactpy.core.types import VdomDict
from reactpy.core.component import Component

CompConstructor = Callable[..., Component]

@component
def For(component: CompConstructor, iterator: Union[List[str], Any]) -> VdomDict:
    """Apply the iterator to the given component

    Usage:

    ```
        users = ["Test User", "Real User 1", "Real User 2"]

        For(html.h2, iterator=users)

        @component
        def TableRow(index:int, row:Any):
            ...

        For(TableRow, iterator=enumerate(users))
    ```
    """

    if isinstance(iterator, List):
        components = [component(name) for name in iterator]
    else:
        components = [component(index, value) for index, value in iterator]

    return html._(*components)
