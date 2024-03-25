from typing import Tuple

from utils.memo import MemoOpts, memo

from ..types import ITable, TableData, TableSearch, TData, TFeatureFactory, UpstreamData, update_state


class DefaultTableSearch(TableSearch[TData]):

    def __init__(self, table: ITable[TData], upstream_data: UpstreamData[TData]):
        super().__init__(table, upstream_data)
        self.search_term: str = ''
        self.case_sensitive: bool = False

        def deps() -> Tuple[TableData[TData], str, bool]:
            return (
                upstream_data(),
                self.search_term,
                self.case_sensitive
            )

        def updater(upstream_data: TableData[TData],
                   search_term: str, case_sensitive:bool
                   ) -> TableData[TData]:

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


        self.pipeline = memo(deps, updater, MemoOpts(name='        4. DefaultTableSearch', debug=True))


    @update_state
    def table_search(self, search_term: str, case_sensitive: bool = False):

        self.case_sensitive = case_sensitive

        if case_sensitive:
            self.search_term = search_term.lower()
        else:
            self.search_term = search_term


def getDefaultTableSearch() -> TFeatureFactory[TData, TableSearch[TData]]:

    def wrapper(table: ITable[TData], updater: UpstreamData[TData]) -> TableSearch[TData]:
        return DefaultTableSearch(table=table, upstream_data=updater)

    return wrapper
