import logging
from typing import Any, Callable, Dict, List

from reactpy import component, event, html, use_memo, use_state

from reactpy_table import ColumnDef, Options, FeatureControl, Table, use_reactpy_table
from utils import For, ServerOptions, pico_run, set_log_level

from .components import Button, Search, TablePaginator, ModalForm
from .data.sp500 import COLS, CompanyModel, get_sp500

log = logging.getLogger(__name__)

# Example supports search, sort & pagination

@component
def THead(table: Table[CompanyModel]):

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

def TRow(index: int, row: CompanyModel, edit_row: Action, delete_row: Action):

    @component
    def Actions():
        return html.td({'class_name': 'grid', 'style': {'align-items': 'center','grid-template-columns': '0.5fr 0.5fr'}},
            Button("row-edit", "📝", lambda : edit_row(index), table_button=True),
            Button("row-edit", "❌", lambda : delete_row(index),  table_button=True),
        )


    return  html.tr({'id': f"row-{index}"},
        Actions(),
        html.td(str(row.index)),
        html.td(row.symbol),
        html.td(row.name),
        html.td(row.sector),
        html.td(row.industry),
        html.td(row.headquarters),
        html.td(row.CIK),
    )


def TBody(table: Table[CompanyModel]):

    rows = table.data.rows
    page_base = table.paginator.page_base

    def delete_row(index:int):
        table.row_model.delete_row(page_base + index)

    def edit_row(index:int):
        row = rows[index].model_copy()
        row.industry = "XXXX"
        table.row_model.update_row(page_base + index, row)


    return  html.tbody(
        [TRow(index, row, edit_row, delete_row) for index, row in enumerate(rows)]
    )


@component
def TFoot(table: Table[CompanyModel]):
    columns = table.data.cols
    return html.tfoot(
        For(html.td, [col.label for col in columns])
    )


@component
def AppMain():

    table_data = use_memo(get_sp500)

    table = use_reactpy_table(options=Options(
        rows=table_data,
        cols = COLS,
        pagination_control=FeatureControl.DEFAULT
    ))

    modal_open, set_modal_open = use_state(False)


    return html.div(
        ModalForm(open=modal_open, set_open=set_modal_open),
        html.br(),
        html.h2('ReactPy Table Example'),
        Search(table.search),
        html.table({"role": "grid"},
            TColgroup([100, 80, 175, 250, 200, 300, 250, 100]),
            THead(table),
            TBody(table),
            TFoot(table),
        ),
        TablePaginator(table.paginator),
    )

# python -m examples.table_example

if __name__ == "__main__":
    set_log_level(logging.INFO)
    pico_run(AppMain, options=ServerOptions(
        head = ["assets/css/modal.css"
        ]))
