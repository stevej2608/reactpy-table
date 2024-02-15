from abc import abstractmethod
from .feature import Feature


class TableSearch(Feature):

    @abstractmethod
    def table_search(self, text:str): ...
