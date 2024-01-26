from reactpy import component, html, run
from reactpy_table import hello_world

@component
def AppMain():
    return html.div(
        hello_world()
    )

# python -m examples.world_example

if __name__ == "__main__":
    run(AppMain)
