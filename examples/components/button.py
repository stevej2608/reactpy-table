from typing import Any, Callable, Dict

from reactpy import component, event, html


# Example supports search, sort & pagination

@component
def Button(id:str, text:str, action: Callable[...,None], disabled: bool=False, table_button: bool=False):

    @event
    def onclick(event: Dict[str, Any]):
        action()

    props: Dict[str,Any] = {'id': id, 'onclick': onclick, 'disabled': disabled}

    if table_button:

        props['style'] = {
            'padding': '0px', 
            'margin-bottom': '0px', 
            'background-color': 'transparent', 
            'border-color': 'transparent'
            }

    return html.button(props, text)
