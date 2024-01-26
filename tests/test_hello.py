import pytest
from reactpy.testing import DisplayFixture

from reactpy_table import hello_world


@pytest.mark.anyio
async def test_sample(display: DisplayFixture):
    await display.show(hello_world)
    h2 = await display.page.wait_for_selector("h2")
    assert (await h2.text_content()) == 'Hello World'

