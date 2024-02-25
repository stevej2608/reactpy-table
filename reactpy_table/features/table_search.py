from ..types import ITable, TableSearch, Updater, update_state, TData, TFeatureFactory


class DefaultTableSearch(TableSearch[TData]):

    @update_state
    def table_search(self, search_term: str, case_sensitive: bool = False):
        if not case_sensitive:
            search_term = search_term.lower()

        def _filter(row: TData):
            row_text = " ".join([str(val) for val in row.model_dump().values()])

            if not case_sensitive:
                row_text = row_text.lower()

            return search_term in row_text

        result = filter(_filter, self.initial_values)
        self.data.rows = list(result)


def getDefaultTableSearch() -> TFeatureFactory[TData, TableSearch[TData]]:

    def wrapper(table: ITable[TData], updater: Updater[TData]) -> TableSearch[TData]:
        return DefaultTableSearch(table=table, updater=updater)

    return wrapper
