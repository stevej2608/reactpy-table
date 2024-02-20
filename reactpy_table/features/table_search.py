from ..types.table_data import Column
from ..types.feature import update_state
from ..types.abstract_table import Table
from ..types.abstract_table import TableSearch


class DefaultTableSearch(TableSearch):


    @staticmethod
    def init(table: Table) -> 'TableSearch':
        search = DefaultTableSearch(table=table)
        return search


    @update_state
    def table_search(self, text:str, case_sensitive:bool=False):

        if not case_sensitive:
            text = text.lower()

        def _filter(element: Column):
            element_text = ' '.join([str(val)  for val in element.model_dump().values()])

            if not case_sensitive:
                element_text = element_text.lower()

            return text in element_text


        result = filter(_filter, self.initial_values)
        self.data.rows = list(result)
