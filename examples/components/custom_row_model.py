
from reactpy_table.features import DefaultRowModel
from reactpy_table.types import ITable, RowModel, TFeatureFactory, Updater, update_state
from ..data.sp500 import CompanyModel

class CustomRowModel(DefaultRowModel[CompanyModel]):

    @update_state
    def delete_row(self, index:int) -> None:
        index = self.table_index(index)
        del self.table.data.rows[index]


    @update_state
    def update_row(self, index:int, row:CompanyModel) -> None:
        index = self.table_index(index)
        self.table.data.rows[index] = row


def getCustomRowModel() -> TFeatureFactory[CompanyModel, RowModel[CompanyModel]]:

    def wrapper(table: ITable[CompanyModel], updater: Updater[CompanyModel]) -> RowModel[CompanyModel]:
        return CustomRowModel(table=table, updater=updater)

    return wrapper
