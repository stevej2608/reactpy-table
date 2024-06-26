import logging
from reactpy import component, html, use_memo

from reactpy_table import Options, Table, use_reactpy_table
from utils import pico_run, For, set_log_level

from .data.sp500 import COLS, CompanyModel, get_sp500

log = logging.getLogger(__name__)

# Minimal example, see table_example.py for search, sort & pagination

@component
def THead(table: Table[CompanyModel]):
    cols = table.data.cols
    return html.thead(
        html.th(cols[0].label),
        html.th(cols[1].label),
        html.th(cols[2].label),
        html.th(cols[3].label)
    )


def TRow(index: int, row: CompanyModel):
    return  html.tr(
        html.td(str(row.index)),
        html.td(row.symbol),
        html.td(row.name),
        html.td(row.sector),
    )

@component
def TBody(table: Table[CompanyModel]):
    rows = table.data.rows
    return  html.tbody(
        For(TRow, iterator=enumerate(rows))
    )

@component
def AppMain():
    table_data = use_memo(lambda:get_sp500(rows=50))
    table = use_reactpy_table(Options(
        rows=table_data,
        cols = COLS,
    ))

    return html.div(
        html.br(),
        html.h2('ReactPy Table Example'),
        html.table({"role": "grid"},
            THead(table),
            TBody(table)
        ),
    )

# python -m examples.basic_example

if __name__ == "__main__":
    set_log_level(logging.INFO)
    pico_run(AppMain)
