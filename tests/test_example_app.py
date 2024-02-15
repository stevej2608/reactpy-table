import pytest
from reactpy.testing import DisplayFixture

from examples.table_example import AppMain


# https://playwright.dev/python/docs/next/locators
# https://playwright.dev/python/docs/next/other-locators#xpath-locator

@pytest.mark.anyio
async def test_paginator(display: DisplayFixture):
    await display.show(AppMain)

    h2 = await display.page.wait_for_selector("h2")

    assert h2 is not None

    assert (await h2.text_content()) == 'ReactPy Table Example'

    # Confirm first row, last row, number of rows  and page display

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('1')

    text = await display.page.locator('id=row-9').all_inner_texts()
    assert text[0].startswith('10')

    rows = await display.page.locator('tr').count()
    assert rows == 10

    text = await display.page.locator('id=pg-pages').all_inner_texts()
    assert text[0] == 'Page 1 of 51'

    # Set page size = 20

    await display.page.select_option('select', label='20')

    # Confirm first row, last row, number of rows and page display

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('1')

    text = await display.page.locator('id=row-19').all_inner_texts()
    assert text[0].startswith('20')

    rows = await display.page.locator('tr').count()
    assert rows == 20

    text = await display.page.locator('id=pg-pages').all_inner_texts()
    assert text[0] == 'Page 1 of 26'

    # Select next page

    pg_next = display.page.locator('id=pg-next')
    await pg_next.click()

    # Confirm first row, last row, number of rows and page display

    rows = await display.page.locator('tr').count()
    assert rows == 20

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('21')

    text = await display.page.locator('id=row-19').all_inner_texts()
    assert text[0].startswith('40')

    text = await display.page.locator('id=pg-pages').all_inner_texts()
    assert text[0] == 'Page 2 of 26'

    # Go to last page

    pg_next = display.page.locator('id=pg-last')
    await pg_next.click()

    rows = await display.page.locator('tr').count()
    assert rows == 5

    # Confirm last row and page display

    text = await display.page.locator('id=row-4').all_inner_texts()
    assert text[0].startswith('505')

    text = await display.page.locator('id=pg-pages').all_inner_texts()
    assert text[0] == 'Page 26 of 26'


@pytest.mark.anyio
async def test_search(display: DisplayFixture):
    await display.show(AppMain)
    h2 = await display.page.wait_for_selector("h2")

    assert h2 is not None

    assert (await h2.text_content()) == 'ReactPy Table Example'

    search = display.page.locator('id=tbl-search')
    await search.fill("Building Products")

    rows = await display.page.locator('tr').count()
    assert rows == 6


@pytest.mark.anyio
async def test_sort(display: DisplayFixture):
    await display.show(AppMain)
    h2 = await display.page.wait_for_selector("h2")

    assert h2 is not None

    assert (await h2.text_content()) == 'ReactPy Table Example'

    search = display.page.locator('id=tbl-sort-#')

    await search.click()
    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('505')

    await search.click()
    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('1')


    search = display.page.locator('id=tbl-sort-sector')
    await search.click()

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('11')
