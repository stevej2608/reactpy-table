import logging
from typing import Any, Callable, Dict, List

from reactpy import component, event, html

from reactpy_table import ColumnDef, Options, FeatureControl, Table, use_reactpy_table
from utils import For, pico_run, set_log_level

from ..components import Button, Search, TablePaginator
from ..hooks import use_pagination, use_sorting, use_search, use_api, DBQuery

from .db import COLS, Book

log = logging.getLogger(__name__)

@component
def THead(table: Table[Book]):

    @component
    def Action():
        return html.th('Action')


    def text_with_arrow(col: ColumnDef):

        sort = table.sort

        @event
        def on_click(event: Dict[str, Any]):
            log.info('on_click col=%s', col)
            sort.toggle_sort(col)

        # https://symbl.cc/en/collections/arrow-symbols/

        up = sort.is_sort_reverse(col)

        text = col.label + (" 🠕" if up else " 🠗")
        return html.th({'id': f'tbl-sort-{col.label.lower()}', 'on_click': on_click}, text)

    columns = table.data.cols

    rows = For(text_with_arrow, iterator=columns)

    # return html.thead(Actions(), rows)

    return html.thead(html._(Action(), rows))


@component
def TColgroup(col_widths: List[int]):
    """Return a html.colgroup with the given widths"""
    return  html.colgroup(
        [html.col({'style': {'width':f"{width}px"}}) for width in col_widths]
    )

Action = Callable[[int], None]

def TRow(index: int, row: Book, edit_row: Action, delete_row: Action):

    @component
    def Actions():
        return html.td({'class_name': 'grid', 'style': {'align-items': 'center','grid-template-columns': '0.5fr 0.5fr'}},
            Button("row-edit", "📝", lambda : edit_row(index), table_button=True),
            Button("row-edit", "❌", lambda : delete_row(index),  table_button=True),
        )


    return  html.tr({'id': f"row-{index}"},
        Actions(),
        html.td(str(row.id)),
        html.td(row.title),
        html.td(row.author),
        html.td(row.publication_date.strftime("%Y-%m-%d")),
        html.td(row.genre),
        html.td(str(row.rating)),
    )


def TBody(table: Table[Book]):

    rows = table.data.rows
    page_base = table.paginator.page_base

    def delete_row(index:int):
        table.row_model.delete_row(page_base + index)

    def edit_row(index:int):
        row = rows[index].model_copy()
        row.author = "XXXX"
        table.row_model.update_row(page_base + index, row)


    return  html.tbody(
        [TRow(index, row, edit_row, delete_row) for index, row in enumerate(rows)]
    )


@component
def TFoot(table: Table[Book]):
    columns = table.data.cols
    return html.tfoot(
        For(html.td, [col.label for col in columns])
    )


@component
def AppMain():

    # Feature state - only needed because the
    # sort, search and pagination is being performed by
    # the SQLite API

    pagination, pagination_change = use_pagination()
    sort, sorting_change = use_sorting()
    search, search_change = use_search()

    table_data, page_count, _loading = use_api(
        url='sqlite:///books.db',
        query=DBQuery(pagination=pagination, sort=sort, search=search)
        )


    table = use_reactpy_table(options=Options(
        rows=table_data,
        cols = COLS,

        pagination_control = FeatureControl.MANUAL,
        on_pagination_change = pagination_change,
        page_count = page_count,

        sort_control = FeatureControl.MANUAL,
        on_sort_change = sorting_change,

        search_control=FeatureControl.MANUAL,
        on_search_change = search_change,

    ))


    log.info('refresh UI')

    return html.div(
        html.br(),
        html.h2('ReactPy SQL Table Example'),
        Search(table.search),
        html.table({"role": "grid"},
            TColgroup([100, 80, 450, 250, 200, 300]),
            THead(table),
            TBody(table),
            TFoot(table),
        ),
        TablePaginator(table.paginator),
    )

# python -m examples.books.books_example

if __name__ == "__main__":
    set_log_level(logging.INFO)
    pico_run(AppMain)
