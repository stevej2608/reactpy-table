from typing import Tuple, cast, List

from utils.memo import memo, MemoOpts
from ..types import ITable, TableSearch, TableData, TData, EMPTY_TABLE, TFeatureFactory, UpstreamData, update_state



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

                row_text = " ".join([str(val) for val in row.model_dump().values()])

                if not self.case_sensitive:
                    row_text = row_text.lower()

                return self.search_term in row_text

            table_data = upstream_data

            if self.search_term:
                rows = cast(List[TData], filter(_filter, table_data.rows))
                return TableData(rows=rows, cols=table_data.cols)
            else:
                return table_data


        self.pipeline = memo(deps, updater, MemoOpts(name='1. DefaultTableSearch'))

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


def getDefaultTableSearch() -> TFeatureFactory[TData, TableSearch[TData]]:

    def wrapper(table: ITable[TData], updater: UpstreamData[TData]) -> TableSearch[TData]:
        return DefaultTableSearch(table=table, upstream_data=updater)

    return wrapper
