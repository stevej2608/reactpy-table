from typing import Any, List
from abc import abstractmethod
from .feature import Feature
from .abstract_table import Table

class Paginator(Feature):

    page_index: int = 0
    """Page index [0..n]"""

    page_size: int


    @staticmethod
    def init(table: Table) -> 'Paginator':
        raise NotImplementedError()


    def __init__(self, table: Table, page_size:int):
        super().__init__(table)
        self.page_size = page_size


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

    @abstractmethod
    def first_page(self): ...

    @abstractmethod
    def previous_page(self): ...

    @abstractmethod
    def next_page(self): ...

    @abstractmethod
    def last_page(self): ...

    @abstractmethod
    def set_page_index(self, page_index:int): ...

    @abstractmethod
    def can_get_previous_page(self) -> bool: ...

    @abstractmethod
    def can_get_next_page(self) -> bool: ...

    @abstractmethod
    def set_page_size(self, page_size:int): ...
