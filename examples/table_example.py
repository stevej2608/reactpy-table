from typing import Any, Callable, Dict, List

from reactpy import component, event, html, use_memo, use_state
from reactpy.core.component import Component

from reactpy_table import ColumnDef, Columns, IPaginator, ITableSearch, Options, Table, use_reactpy_table
from utils.logger import log, logging
from utils.pico_run import pico_run, ServerOptions
from utils.reactpy_helpers import For
from utils.types import EventArgs

from .data.sp500 import COLS, CompanyModel, get_sp500

# Example supports search, sort & pagination

@component
def Button(id:str, text:str, action: Callable[...,None], disabled: bool=False, table_button: bool=False):

    @event
    def onclick(event: Dict[str, Any]):
        action()

    props: Dict[str,Any] = {'id': id, 'onclick': onclick, 'disabled': disabled}

    if table_button:

        props['style'] = {
            'padding': '0px', 
            'margin-bottom': '0px', 
            'background-color': 'transparent', 
            'border-color': 'transparent'
            }

    return html.button(props, text)


@component
def TablePaginator(paginator: IPaginator[CompanyModel]):

    @component
    def PageSizeSelect(sizes:List[int]):

        @event
        def on_change(event: Dict[str, Any]):
            page_size = int(event['currentTarget']['value'])
            paginator.set_page_size(page_size)


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
    def Action():
        return html.th('Action')


    def text_with_arrow(col: ColumnDef):

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

    rows = For(text_with_arrow, iterator=columns)

    # return html.thead(Actions(), rows)

    return html.thead(html._(Action(), rows))


@component
def TColgroup(col_widths: List[int]):
    """Return a html.colgroup with the given widths"""
    return  html.colgroup(
        [html.col({'style': {'width':f"{width}px"}}) for width in col_widths]
    )


def TRow(index: int, row: CompanyModel):

    def delete_row():
        log.info('delete %d', row.index)

    def edit_row():
        log.info('delete %s', row.index)

    @component
    def Actions():
        return html.td({'class_name': 'grid', 'style': {'align-items': 'center','grid-template-columns': '0.5fr 0.5fr'}},
            Button("row-edit", "📝", edit_row, table_button=True),
            Button("row-edit", "❌", delete_row,  table_button=True),
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


def TBody(table: List[CompanyModel]):
    return  html.tbody(
        For(TRow, iterator=enumerate(table))
    )


@component
def TFoot(columns: Columns):
    return html.tfoot(
        For(html.td, [col.label for col in columns])
    )


# https://picocss.com/docs/modal

@component
def ModalForm(open: bool, set_open: Callable[[bool], None]):

    @event(prevent_default=True)
    def close(event: EventArgs):
        set_open(False)


    return html.dialog({"open": open, "on_click": close},
        html.article(
            html.header(
                html.button({"aria-label": "Close", "rel": "prev"}, "✕"),
                html.p(html.strong("🗓️ Thank You for Registering!")),
            ),
            html.p("""
                   We're excited to have you join us for our upcoming event. 
                   Please arrive at the museum  on time to check in and 
                   get started."""),
            html.ul(html.li("Date: Saturday, April 15"), html.li("Time: 10:00am - 12:00pm")),
        ),
    )


@component
def AppMain():

    table_data = use_memo(get_sp500)

    table = use_reactpy_table(options=Options(
        rows=table_data,
        cols = COLS
    ))

    modal_open, set_modal_open = use_state(True)


    return html.div(
        ModalForm(open=modal_open, set_open=set_modal_open),
        html.br(),
        html.h2('ReactPy Table Example'),
        Search(table.search),
        html.table({"role": "grid"},
            TColgroup([100, 80, 175, 250, 200, 300, 250, 100]),
            THead(table),
            TBody(table.paginator.rows),
            TFoot(table.data.cols),
        ),
        TablePaginator(table.paginator),
    )

# python -m examples.table_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)

    opt = ServerOptions(
        head = [
            html.title('XXX'),
            "assets/css/modal.css"
            ]
    )

    pico_run(AppMain, options=opt)
