from typing import Any, Callable, Dict, List

from reactpy import component, event, html, use_memo, use_state
from reactpy.core.component import Component

from reactpy_table import Column, Columns, IPaginator, ITableSearch, Options, Table, use_reactpy_table
from utils.logger import log, logging
from utils.pico_run import pico_run
from utils.reactpy_helpers import For

from .data.sp500 import COLS, CompanyModel, get_sp500

# Example supports search, sort & pagination


@component
def TablePaginator(paginator: IPaginator[CompanyModel]):

    @component
    def Button(id:str, text:str, action: Callable[...,None], disabled: bool=False):

        @event
        def onclick(event: Dict[str, Any]):
            action()

        return html.button({'id': id, 'onclick': onclick, 'disabled': disabled}, text)

    @component
    def PageSizeSelect(sizes:List[int]):

        @event
        def on_change(event: Dict[str, Any]):
            page_size = int(event['currentTarget']['value'])
            paginator.set_page_size(page_size)

        @component
        def PageOption(size:int):
            return html.option({'value': size}, f"{size}")

        return html.select({'id': 'dd1', 'value': sizes[0], "on_change": on_change}, For(PageOption, sizes))


    @component
    def PageInput():

        count_value, set_count = use_state(0)

        @event(prevent_default=True)
        def on_change(event: Dict[str, Any]):

            try:
                new_value = int(event['currentTarget']['value'])
                new_value = max(new_value, 1)
                new_value = min(new_value, paginator.page_count)
            except Exception:
                new_value = 1

            log.info('new_value = %d', new_value)

            if paginator.page_index != new_value - 1:
                paginator.set_page_index(new_value - 1)
            else:
                set_count(count_value + 1)

        log.info('render new_value = %d', paginator.page_index + 1)

        return html._(
            Text("Go to page:"),
            html.input({'type': 'number', 'value': paginator.page_index + 1, "on_change": on_change}),
        )

    no_previous = not paginator.can_get_previous_page()
    no_next = not paginator.can_get_next_page()

    return html.div({'class_name': 'grid', 'style': {'align-items': 'center','grid-template-columns': '2.5fr 1.5fr 1.5fr 2.5fr 4fr 1.2fr 2fr 3fr'}},
        Button("pg-first", "<<", paginator.first_page, disabled = no_previous),
        Button("pg-prev", "<", paginator.previous_page, disabled = no_previous),
        Button("pg-next", ">", paginator.next_page, disabled = no_next),
        Button("pg-last", ">>", paginator.last_page, disabled = no_next),
        Text("Page",html.strong(f" {paginator.page_index + 1} of {paginator.page_count}")),
        PageInput(),
        PageSizeSelect([10, 20, 30, 40, 50])
    )


@component
def Text(*children: List[Component]):
    """Add the pico button margin to make the 
    given text line up with the button text."""

    return html.span({'id': 'pg-pages','style': 'margin-bottom: var(--spacing);'}, *children)


@component
def Search(search: ITableSearch[CompanyModel]):

    @event
    def on_change(event: Dict[str, Any]):
        text = event['currentTarget']['value']
        search.table_search(text)

    return html.input({'id':'tbl-search', 'type': 'search', 'placeholder': 'Search', 'aria-label': 'Search', 'onchange': on_change})

@component
def THead(table: Table[CompanyModel]):

    @component
    def text_with_arrow(col: Column):

        sort = table.sort

        @event
        def on_click(event: Dict[str, Any]):
            log.info('onclick col=%s', col)
            sort.toggle_sort(col)

        # https://symbl.cc/en/collections/arrow-symbols/

        up = sort.is_sort_reverse(col)

        text = col.label + (" 🠕" if up else " 🠗")
        return html.th({'id': f'tbl-sort-{col.label.lower()}', 'onclick': on_click}, text)

    columns = table.data.cols

    return html.thead(
        For(text_with_arrow, iterator=columns)
    )


@component
def TColgroup(col_widths: List[int]):
    """Return a html.colgroup with the given widths"""
    return  html.colgroup(
        [html.col({'style': {'width':f"{width}px"}}) for width in col_widths]
    )


@component
def TRow(index: int, row: CompanyModel):
    return  html.tr({'id': f"row-{index}"},
        html.td(str(row.index)),
        html.td(row.symbol),
        html.td(row.name),
        html.td(row.sector),
        html.td(row.industry),
        html.td(row.headquarters),
        html.td(row.CIK),
    )


def TBody(table: List[CompanyModel]):
    return  html.tbody(
        For(TRow, iterator=enumerate(table))
    )


@component
def TFoot(columns: Columns):
    return html.tfoot(
        For(html.td, [col.label for col in columns])
    )


@component
def AppMain():

    table_data = use_memo(get_sp500)

    table = use_reactpy_table(options=Options(
        rows=table_data,
        cols = COLS
    ))


    return html.div(
        html.br(),
        html.h2('ReactPy Table Example'),
        Search(table.search),
        html.table({"role": "grid"},
            TColgroup([80, 150, 250, 200, 300, 250, 100]),
            THead(table),
            TBody(table.paginator.rows),
            TFoot(table.data.cols),
        ),
        TablePaginator(table.paginator)
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    pico_run(AppMain)
