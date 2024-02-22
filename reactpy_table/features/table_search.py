from ..types import ITable, TableSearch, Updater, update_state, RowData

class DefaultTableSearch(TableSearch):


    @staticmethod
    def init(table: ITable, updater:Updater) -> TableSearch:
        search = DefaultTableSearch(table=table, updater=updater)
        return search


    @update_state
    def table_search(self, text:str, case_sensitive:bool=False):

        if not case_sensitive:
            text = text.lower()

        def _filter(element: RowData):
            element_text = ' '.join([str(val)  for val in element.model_dump().values()])

            if not case_sensitive:
                element_text = element_text.lower()

            return text in element_text


        result = filter(_filter, self.initial_values)
        self.data.rows = list(result)
