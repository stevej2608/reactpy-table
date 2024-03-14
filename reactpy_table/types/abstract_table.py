from typing import Generic, Protocol

from .table_data import TableData, TData


class ITable(Generic[TData], Protocol):

    @property
    def data(self) -> TableData[TData]:
        """Return data for presentation by the user"""
        ... # pylint: disable=unnecessary-ellipsis
