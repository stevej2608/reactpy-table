from typing import Any, Dict

from reactpy import component, event, html

from reactpy_table import ITableSearch

from ..data.sp500 import CompanyModel


@component
def Search(search: ITableSearch[CompanyModel]):

    @event
    def on_change(event: Dict[str, Any]):
        text = event['currentTarget']['value']
        search.table_search(text)

    return html.input({'id':'tbl-search', 'type': 'search', 'placeholder': 'Search', 'aria-label': 'Search', 'onchange': on_change})
