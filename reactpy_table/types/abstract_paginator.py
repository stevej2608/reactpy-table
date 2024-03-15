from typing import Protocol, cast, Callable, Any

from .abstract_table import ITable
from .feature import FeatureBase, IFeature
from .table_data import TData, TableData
from .updater import Updater

# pyright: reportReturnType=false


class IPaginator(IFeature[TData], Protocol):

    # https://tanstack.com/table/v8/docs/api/features/pagination

    @property
    def page_index(self) -> int:
        """Page index [0..n]"""

    @property
    def page_size(self) -> int:
        """Current page size"""

    @property
    def page_base(self) -> int:
        """Table index of first row in the page"""


    @property
    def page_count(self) -> int:
        """Return number of pages"""

    @property
    def row_count(self) -> int:
        """Return total number of rows"""

    def first_page(self):
        """Goto first page"""

    def previous_page(self):
        """Decrements the page index by one, if possible."""

    def next_page(self):
        """Increments the page index by one, if possible."""

    def last_page(self):
        """Goto last page"""

    def set_page_index(self, page_index: int):
        """Go to specific page if possible [0..n]"""

    def can_get_previous_page(self) -> bool:
        """Returns true if previous page exits"""

    def can_get_next_page(self) -> bool:
        """Returns true if next page exits"""

    def set_page_size(self, page_size: int):
        """Set the page size"""


class Paginator(IPaginator[TData], FeatureBase[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData]):
        super().__init__(table=table, updater=updater)

        self.upstream: Callable[[], TableData[TData]] = cast(Any, table).row_model.pipeline
