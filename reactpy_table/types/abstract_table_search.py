from typing import Protocol

from .feature import IFeature, FeatureBase
from .abstract_table import TData


class ITableSearch(IFeature[TData], Protocol):
    def table_search(self, search_term: str, case_sensitive: bool = False):
        ...


class TableSearch(ITableSearch[TData], FeatureBase[TData]):
    pass
