from typing import Tuple

from utils.memo import memo
from ..types import ITable, TableSearch, TableData, TData, EMPTY_TABLE, TFeatureFactory, Updater, update_state



class DefaultTableSearch(TableSearch[TData]):

    def __init__(self, table: ITable[TData], updater: Updater[TData]):
        super().__init__(table, updater)
        self.search_term: str = ''
        self.case_sensitive: bool = False
        self.pipeline = memo(
            self.get_deps,
            self.expensive_computation,
            {'onChange': self.on_change}
            )


    def get_deps(self) -> Tuple[int, int]:
        return (1, 2)

    def expensive_computation(self, a: int, b: int) -> TableData[TData]:
        return EMPTY_TABLE

    def on_change(self, result: int):
        print(f"Result changed: {result}")

    @update_state
    def table_search(self, search_term: str, case_sensitive: bool = False):

        self.case_sensitive = case_sensitive

        if case_sensitive:
            self.search_term = search_term.lower()
        else:
            self.search_term = search_term


    # def pipeline(self, table_data:TableData[TData]) -> TableData[TData]:

    #     def _filter(row: TData) -> bool:

    #         row_text = " ".join([str(val) for val in row.model_dump().values()])

    #         if not self.case_sensitive:
    #             row_text = row_text.lower()

    #         return self.search_term in row_text


    #     if self.search_term:
    #         rows = cast(List[TData], filter(_filter, table_data.rows))
    #         return TableData(rows=rows, cols=table_data.cols)
    #     else:
    #         return table_data


def getDefaultTableSearch() -> TFeatureFactory[TData, TableSearch[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> TableSearch[TData]:
        return DefaultTableSearch(table=table, updater=updater)

    return wrapper
