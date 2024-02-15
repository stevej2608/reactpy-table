from typing import List
import pytest
from reactpy import html, component, Layout, use_memo
from reactpy_table import use_reactpy_table, Columns, Options, SimplePaginator, SimpleColumnSort, SimpleTableSearch

from .data.users import make_data, DataModel


@pytest.mark.anyio
async def test_make_data():
    rows = make_data(100)
    assert rows[0].index == 0
    assert rows[99].name == "Stark Cote"


@pytest.mark.anyio
async def test_use_memo():
    rows: List[DataModel] = []

    @component
    def TestComponent():
        nonlocal rows
        table_data = use_memo(lambda: make_data(100))
        rows += table_data
        return html.div()

    async with Layout(TestComponent()) as layout:
        await layout.render()
        assert rows[0].index == 0
        assert rows[99].name == "Stark Cote"


@pytest.mark.anyio
async def test_basic_usage():
    COLS: Columns = []
    table = None

    @component
    def TestComponent():
        nonlocal table
        table = use_reactpy_table(Options(
            rows=make_data(100),
            cols = COLS,
            plugins=[
                SimplePaginator.init,
                SimpleColumnSort.init,
                SimpleTableSearch.init
                ]
        ))
        return html.div()

    async with Layout(TestComponent()) as layout:
        await layout.render()
        assert table
