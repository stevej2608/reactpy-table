from typing import Callable, Any
import sys
import os
import inspect
from pathlib import Path
import uvicorn
from fastapi import FastAPI
from reactpy import html
from reactpy.core.component import Component
from reactpy.backend.fastapi import configure, Options as FastApiOptions

from utils.logger import log, logging
from utils.var_name import var_name

from utils.assets import assets_api
from utils.options import ServerOptions, DEFAULT_OPTIONS

# pyright: reportDeprecated=false
# pyright: reportUnusedFunction=false

app = FastAPI(description="ReactPy", version="0.1.0")


def run(AppMain: Callable[[], Component],
        options:ServerOptions=DEFAULT_OPTIONS,
        host: str='127.0.0.1',
        port: int=8000,
        disable_server_logs: bool=False,
        **kwargs: Any) -> None:

    """Called once to run reactpy application on the fastapi server

    Args:
        AppMain (Callable[[], Component]): Function that returns a reactpy Component
        options (Options, optional): Server options. Defaults to DASHBOARD_OPTIONS.

    Usage:
    ```
            @component
            def AppMain():
                return html.h2('Hello from reactPy!')
                )

            run(AppMain, options=PICO_OPTIONS)

    ```
    """

    def _app_path(app: FastAPI) -> str:
        app_str = var_name(app, globals())
        return f"{__name__}:{app_str}"

    # Mount any fastapi end points here

    if options.asset_folder == 'assets':
        asset_folder = Path(inspect.stack()[1].filename).parent.relative_to(os.getcwd())
        options.asset_folder = str(asset_folder)

    app.mount("/" + options.asset_root, assets_api(options))

    opt = FastApiOptions(
       head=html.head(*options.head)
    )

    configure(app, AppMain, options=opt)

    app_path = _app_path(app)

    try:
        log.setLevel(logging.INFO)
        uvicorn.run(app_path, host=host, port=port, **kwargs)
    except Exception as ex:
        log.info('Uvicorn server %s\n', ex)
    finally:
        print('\b\b')
        log.info('Uvicorn server has shut down\n')
        sys.exit(0)
