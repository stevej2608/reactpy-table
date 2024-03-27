from typing import Any, Dict, List

from reactpy import component, event, html, use_state

from reactpy_table import IPaginator
from utils import For, log

from ..data.sp500 import CompanyModel
from .button import Button
from .text import Text


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
