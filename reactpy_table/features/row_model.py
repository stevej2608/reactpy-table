from ..types.feature import Updater
from ..types.abstract_row_model import RowModel
from ..types.abstract_table import Table

class SimpleRowModel(RowModel):

    @staticmethod
    def init(table: Table, updater: Updater) -> None:
        table.row_model = SimpleRowModel(
            data=table.data,
            updater = updater
            )
