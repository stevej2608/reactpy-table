from typing import Generic, Protocol

from .table_data import TableData, TData

# pylint: disable=W2301

class ITable(Generic[TData], Protocol):

    @property
    def data(self) -> TableData[TData]:
        """Return data for presentation by the user"""
        ...
