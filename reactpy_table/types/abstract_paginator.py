from typing import Any, List, Protocol
from abc import abstractmethod

from .feature import IFeature, FeatureBase, Updater
from .abstract_table import ITable

class IPaginator(IFeature, Protocol):

    page_index: int = 0
    """Page index [0..n]"""

    page_size: int

    @property
    @abstractmethod
    def rows(self) -> List[Any]:
        """Return rows in current page"""

    @property
    @abstractmethod
    def page_count(self) -> int :
        """Return number of pages"""

    @property
    @abstractmethod
    def row_count(self) -> int :
        """Return total number of rows"""

    def first_page(self): ...

    def previous_page(self): ...

    def next_page(self): ...

    def last_page(self): ...

    def set_page_index(self, page_index:int): ...

    def can_get_previous_page(self) -> bool: ...

    def can_get_next_page(self) -> bool: ...

    def set_page_size(self, page_size:int): ...


class Paginator(IPaginator, FeatureBase):

    @staticmethod
    def init(table: ITable, updater:Updater) -> IPaginator:
        raise NotImplementedError()
