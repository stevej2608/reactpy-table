from typing import cast, List
from ..types import ITable, TableSearch, Updater, update_state, RowData, TRowModel

class DefaultTableSearch(TableSearch[TRowModel]):


    @staticmethod
    def init(table: ITable[TRowModel], updater:Updater[TRowModel]) -> TableSearch[TRowModel]:
        search = DefaultTableSearch(table=table, updater=updater)
        return search


    @update_state
    def table_search(self, search_term:str, case_sensitive:bool=False):

        if not case_sensitive:
            search_term = search_term.lower()

        def _filter(row: RowData):
            row_text = ' '.join([str(val)  for val in row.model_dump().values()])

            if not case_sensitive:
                row_text = row_text.lower()

            return search_term in row_text


        result = filter(_filter, self.initial_values)
        self.data.rows = cast(List[TRowModel],list(result))
