from typing  import Type

from .table_data import TableData

from .abstract_row_model import RowModel
from .abstract_paginator import Paginator
from .abstract_column_sort import ColumnSort
from .abstract_table_search import TableSearch
from .feature import Feature


class Table:

    data: TableData

    paginator: Paginator
    sort: ColumnSort
    search: TableSearch
    row_model: RowModel

    def __init__(self,
                data: TableData,
                paginator: Type[Paginator],
                sort: Type[ColumnSort],
                search: Type[TableSearch],
                row_model: Type[RowModel]
                ):

        self.data = data
        self.paginator = paginator.init(self)
        self.sort = sort.init(self)
        self.search = search.init(self)
        self.row_model = row_model.init(self)

        # self.updater: Callable[[Any], None] = lambda self: None
        # self.updater: Callable[[Any, Feature], None] = lambda self, feature: None

    def updater(self, feature: Feature):
        ...
