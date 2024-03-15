
from reactpy_table.features import DefaultRowModel
from reactpy_table.types import ITable, RowModel, TData, TFeatureFactory, Updater, update_state


class CustomRowModel(DefaultRowModel[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData]):
        super().__init__(table=table, updater=updater)

    @update_state
    def delete_row(self, index:int) -> None:
        index = self.table_index(index)
        del self.table.data.rows[index]


    @update_state
    def update_row(self, index:int, row:TData) -> None:
        index = self.table_index(index)
        self.table.data.rows[index] = row


    # def pipeline(self, table_data:TableData[CompanyModel]) -> TableData[CompanyModel]:
    #     return table_data


def getCustomRowModel() -> TFeatureFactory[TData, RowModel[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> RowModel[TData]:
        return CustomRowModel(table=table, updater=updater)

    return wrapper
