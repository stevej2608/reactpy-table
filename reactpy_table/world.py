from reactpy import html, component


@component
def hello_world():
    return html.h2('Hello World')
