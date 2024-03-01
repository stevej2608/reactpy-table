import pytest
from reactpy.testing import DisplayFixture

from examples.table_example import AppMain


# https://playwright.dev/python/docs/next/locators
# https://playwright.dev/python/docs/next/other-locators#xpath-locator


async def get_cell_text(display:DisplayFixture, row:int, cell:int) -> str:
    text = await display.page.locator(f"id=row-{row}").all_inner_texts()
    return text[0].split('\t')[cell]

async def get_row_index(display:DisplayFixture, row:int) -> int:
    text = await display.page.locator(f"id=row-{row}").all_inner_texts()
    return int(text[0].split('\t')[1])


@pytest.mark.anyio
async def test_paginator(display: DisplayFixture):

    await display.show(AppMain)

    h2 = await display.page.wait_for_selector("h2")

    assert h2 is not None

    assert (await h2.text_content()) == "ReactPy Table Example"

    # Confirm first row, last row, number of rows  and page display

    index = await get_row_index(display, 0)
    assert index == 1

    index = await get_row_index(display, 9)
    assert index == 10

    rows = await display.page.locator("tr").count()
    assert rows == 10

    text = await display.page.locator("id=pg-pages").all_inner_texts()
    assert text[0] == "Page 1 of 51"

    # Set page size = 20

    await display.page.select_option("select", label="20")

    # Confirm first row, last row, number of rows and page display

    index = await get_row_index(display, 0)
    assert index == 1

    index = await get_row_index(display, 19)
    assert index == 20

    rows = await display.page.locator("tr").count()
    assert rows == 20

    text = await display.page.locator("id=pg-pages").all_inner_texts()
    assert text[0] == "Page 1 of 26"

    # Select next page

    pg_next = display.page.locator("id=pg-next")
    await pg_next.click()

    # Confirm first row, last row, number of rows and page display

    rows = await display.page.locator("tr").count()
    assert rows == 20

    index = await get_row_index(display, 0)
    assert index == 21

    index = await get_row_index(display, 19)
    assert index == 40

    text = await display.page.locator("id=pg-pages").all_inner_texts()
    assert text[0] == "Page 2 of 26"

    # Go to last page

    pg_next = display.page.locator("id=pg-last")
    await pg_next.click()

    rows = await display.page.locator("tr").count()
    assert rows == 5

    # Confirm last row and page display

    index = await get_row_index(display, 4)
    assert index == 505


    text = await display.page.locator("id=pg-pages").all_inner_texts()
    assert text[0] == "Page 26 of 26"


@pytest.mark.anyio
async def test_search(display: DisplayFixture):
    await display.show(AppMain)
    h2 = await display.page.wait_for_selector("h2")

    assert h2 is not None

    assert (await h2.text_content()) == "ReactPy Table Example"

    search = display.page.locator("id=tbl-search")
    await search.fill("Building Products")

    rows = await display.page.locator("tr").count()
    assert rows == 6


@pytest.mark.anyio
async def test_sort(display: DisplayFixture):
    await display.show(AppMain)
    h2 = await display.page.wait_for_selector("h2")

    assert h2 is not None

    assert (await h2.text_content()) == "ReactPy Table Example"

    search = display.page.locator("id=tbl-sort-#")

    await search.click()
    index = await get_row_index(display, 0)
    assert index == 505

    await search.click()
    index = await get_row_index(display, 0)
    assert index == 1

    search = display.page.locator("id=tbl-sort-sector")

    await search.click()
    index = await get_row_index(display, 0)
    assert index == 11
