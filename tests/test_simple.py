from typing import List
import pytest
from reactpy import html, component, use_memo
from reactpy.core.layout import Layout
from reactpy.core._life_cycle_hook import HOOK_STACK
from reactpy_table import use_reactpy_table, Columns, Options

from .data.users import make_data, DataModel


async def test_make_data():
    rows = make_data()
    assert rows[0].index == 0
    assert rows[99].name == "Stark Cote"



async def test_use_memo():
    rows: List[DataModel] = []

    @component
    def TestComponent():
        nonlocal rows
        table_data = use_memo(make_data)
        rows += table_data
        return html.div()

    # Initialize the hook stack context for ReactPy v2
    HOOK_STACK._state.set([])
    async with Layout(TestComponent()) as layout:
        await layout.render()
        assert rows[0].index == 0
        assert rows[99].name == "Stark Cote"



async def test_basic_usage():
    COLS: Columns = []
    table = None

    @component
    def TestComponent():
        nonlocal table
        table = use_reactpy_table(
            Options(
                rows=make_data(),
                cols=COLS,
            )
        )
        return html.div()

    # Initialize the hook stack context for ReactPy v2
    HOOK_STACK._state.set([])
    async with Layout(TestComponent()) as layout:
        await layout.render()
        assert table
