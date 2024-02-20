from ..types.abstract_row_model import RowModel
from ..types.abstract_table import Table

class DefaultRowModel(RowModel):

    @staticmethod
    def init(table: Table) -> RowModel:
        return DefaultRowModel(table=table)
