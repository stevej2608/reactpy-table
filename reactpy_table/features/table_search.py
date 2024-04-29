from typing import Tuple

from reactpy_table.utils.memo import MemoOpts, memo

from ..types import ITable, TableData, TableSearch, SearchState, TData, TFeatureFactory, UpstreamData


class DefaultTableSearch(TableSearch[TData]):

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData]):
        super().__init__(table)
        self._search_state = SearchState()


        def deps() -> Tuple[TableData[TData], SearchState]:
            return (
                upstream_data(),
                self._search_state,
            )

        def updater(upstream_data: TableData[TData],
                   state: SearchState
                   ) -> TableData[TData]:

            case_sensitive = state.case_sensitive
            search_term = state.search_term

            def _filter(row: TData) -> bool:
                nonlocal search_term

                row_text = " ".join([str(val) for val in row.model_dump().values()])

                if not case_sensitive:
                    row_text = row_text.lower()

                return search_term in row_text

            table_data = upstream_data

            if search_term:

                if not case_sensitive:
                    search_term = search_term.lower()

                rows = list(filter(_filter, table_data.rows))
                return TableData(rows=rows, cols=table_data.cols)
            else:
                return table_data


        self.pipeline = memo(deps, updater, MemoOpts(name='        4. DefaultTableSearch', debug=False))


    # @update_state
    def table_search(self, search_term: str, case_sensitive: bool = False):

        new_state = SearchState(search_term=search_term, case_sensitive=case_sensitive)

        if new_state != self._search_state:
            self._search_state = new_state

            if self.table.table_state.on_search_change:
                self.table.table_state.on_search_change(new_state)
            else:
                self.refresh()


def getDefaultTableSearch() -> TFeatureFactory[TData, TableSearch[TData]]:

    def wrapper(table: ITable[TData], updater: UpstreamData[TData]) -> TableSearch[TData]:
        return DefaultTableSearch(table=table, upstream_data=updater)

    return wrapper
