from typing import Generic, Protocol, Callable, Self
from utils.memo import TMemoResult
from .table_data import TableData, TData
from ..core.core_options import CoreTableOptions


class ITable(Generic[TData], Protocol):

    @property
    def data(self) -> TableData[TData]:
        """Return data for presentation by the user"""
        ... # pylint: disable=unnecessary-ellipsis

    @property
    def initial_data(self) -> TableData[TData]:
        """Return data for presentation by the user"""
        ... # pylint: disable=unnecessary-ellipsis

    @property
    def table_options(self) -> CoreTableOptions[TData]:
        """Return the table options"""
        ... # pylint: disable=unnecessary-ellipsis


    def refresh(self) -> Self:
        """Force refresh of the table"""
        ... # pylint: disable=unnecessary-ellipsis


class IPipeline(Protocol, Generic[TMemoResult]):
    pipeline: Callable[[], TMemoResult]


class ITablePipeline(ITable[TData], Protocol, Generic[TData]):

    paginator : IPipeline[TableData[TData]]
    search : IPipeline[TableData[TData]]
    sort : IPipeline[TableData[TData]]
    row_model : IPipeline[TableData[TData]]
