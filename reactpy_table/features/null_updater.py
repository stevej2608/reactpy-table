from typing import Tuple

from utils.memo import memo

from ..types import TableData, TData, UpstreamData


def null_updater(upstream_data: UpstreamData[TData]):
    """Returns a memo that returns the upstream data"""

    def _null_deps() -> Tuple[TableData[TData], int]:
        return (upstream_data(), 0)


    def _null_updater(upstream_data: TableData[TData], _:int) -> TableData[TData]:
        return upstream_data

    return memo(_null_deps, _null_updater)
