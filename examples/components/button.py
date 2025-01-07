from typing import Any, Callable, Dict

from reactpy import component, event, html


# Example supports search, sort & pagination

@component
def Button(id:str, text:str, action: Callable[...,None], disabled: bool=False, table_button: bool=False):

    @event
    def on_click(event: Dict[str, Any]):
        action()

    props: Dict[str,Any] = {'id': id, 'on_click': on_click, 'disabled': disabled}

    if table_button:

        props['style'] = {
            'padding': '0px', 
            'margin-bottom': '0px', 
            'background-color': 'transparent', 
            'border-color': 'transparent'
            }

    return html.button(props, text)
