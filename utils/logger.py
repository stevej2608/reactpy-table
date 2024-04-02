import logging

logging.basicConfig(
    format='%(levelname)s %(asctime)s.%(msecs)03d %(module)20s/%(lineno)-5d %(message)s',
    datefmt='%H:%M:%S'
)

NOISY_LOGS = [
    "asgi-logger",
    "asyncio",
    "charset_normalizer",
    "concurrent.futures",
    "concurrent",
    "faker.factory",
    "faker",
    "fastapi",
    "reactpy._option",
    "reactpy.backend.starlette",
    "reactpy.backend.utils",
    "reactpy.backend",
    "reactpy.core.hooks",
    "reactpy.core.layout",
    "reactpy.core.serve",
    "reactpy.core",
    "reactpy.web.module",
    "reactpy.web.utils",
    "reactpy.web",
    "reactpy",
    "requests",
    "sqlalchemy.dialects.postgresql",
    "sqlalchemy.dialects",
    "sqlalchemy.orm.mapper.Mapper",
    "sqlalchemy.orm.mapper",
    "sqlalchemy.orm.path_registry",
    "sqlalchemy.orm.properties.ColumnProperty",
    "sqlalchemy.orm.properties",
    "sqlalchemy.orm.query.Query",
    "sqlalchemy.orm.query",
    "sqlalchemy.orm.relationships.RelationshipProperty",
    "sqlalchemy.orm.relationships",
    "sqlalchemy.orm.strategies.ColumnLoader",
    "sqlalchemy.orm.strategies.DeferredColumnLoader",
    "sqlalchemy.orm.strategies.DoNothingLoader",
    "sqlalchemy.orm.strategies.ExpressionColumnLoader",
    "sqlalchemy.orm.strategies.JoinedLoader",
    "sqlalchemy.orm.strategies.LazyLoader",
    "sqlalchemy.orm.strategies.NoLoader",
    "sqlalchemy.orm.strategies.SelectInLoader",
    "sqlalchemy.orm.strategies.SubqueryLoader",
    "sqlalchemy.orm.strategies",
    "sqlalchemy.orm.writeonly.WriteOnlyLoader",
    "sqlalchemy.orm.writeonly",
    "sqlalchemy.orm",
    "sqlalchemy",
    "starlette",
    "urllib3.connection",
    "urllib3.connectionpool",
    "urllib3.poolmanager",
    "urllib3.response",
    "urllib3.util.retry",
    "urllib3.util",
    "urllib3",
    "uvicorn.access",
    "uvicorn.error",
    "uvicorn",
    "watchfiles.main",
    "watchfiles.watcher",
    "watchfiles",
]


def disable_noisy_logs():
    # Turn off noisy logging

    for log_id in NOISY_LOGS:
        _log = logging.getLogger(log_id)
        _log.setLevel(logging.ERROR)


def set_log_level(level:int):
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for logger in loggers:
        if logger.name not in NOISY_LOGS:
            # print(f"  \"{logger.name}\",")
            logger.setLevel(level)
