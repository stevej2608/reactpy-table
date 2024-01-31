import pytest
from reactpy.testing import DisplayFixture
from examples.table_example import AppMain

# https://playwright.dev/python/docs/next/locators
# https://playwright.dev/python/docs/next/other-locators#xpath-locator

@pytest.mark.anyio
async def test_sample(display: DisplayFixture):
    await display.show(AppMain)
    h2 = await display.page.wait_for_selector("h2")
    assert (await h2.text_content()) == 'ReactPy Table Example'

    # Confirm first row, last row and number of rows

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('1')

    text = await display.page.locator('id=row-9').all_inner_texts()
    assert text[0].startswith('10')

    rows = await display.page.locator('tr').count()
    assert rows == 10

    # Set page size = 20

    await display.page.select_option('select', label='20')

    # Confirm first row, last row and number of rows

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('1')

    text = await display.page.locator('id=row-19').all_inner_texts()
    assert text[0].startswith('20')

    rows = await display.page.locator('tr').count()
    assert rows == 20

    # Select next page

    pg_next = display.page.locator('id=pg-next')
    await pg_next.click()

    # Confirm first row, last row and number of rows

    rows = await display.page.locator('tr').count()
    assert rows == 20

    text = await display.page.locator('id=row-0').all_inner_texts()
    assert text[0].startswith('21')

    text = await display.page.locator('id=row-19').all_inner_texts()
    assert text[0].startswith('40')

    # Go to last page

    pg_next = display.page.locator('id=pg-last')
    await pg_next.click()

    rows = await display.page.locator('tr').count()
    assert rows == 5

    # Confirm last row

    text = await display.page.locator('id=row-4').all_inner_texts()
    assert text[0].startswith('505')
