from typing import List, Any
from abc import abstractmethod
from .abstract_plugin import Plugin


class Paginator(Plugin):

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
