## reactpy-table

![](https://raw.githubusercontent.com/stevej2608/reactpy-table/master/docs/img/screenshot.png)

Headless UI for building powerful tables with [ReactPy]. The project 
takes its design ideas from the hugely popular, ReactJS based, [TanStack Table].

The initial release supports the following features:

- [X] Headless UI, CSS agnostic
- [X] Freeform text search
- [X] Forward/Reverse column based sort
- [X] Pagination
- [ ] Integration with Pandas (in progress)
- [ ] Remote large dataset support

## Usage

	pip install reactpy-table

*[basic_example.py](examples/basic_example.py)*
```
@component
def THead(table: Table):
    cols = table.data.cols
    return html.thead(
        html.th(cols[0].label),
        html.th(cols[1].label),
        html.th(cols[2].label),
        html.th(cols[3].label)
    )

@component
def TRow(index: int, row: CompanyModel):
    return  html.tr(
        html.td(str(row.index)),
        html.td(row.symbol),
        html.td(row.name),
        html.td(row.sector),
    )

@component
def TBody(table: List[CompanyModel]):
    return  html.tbody(
        For(TRow, iterator=enumerate(table))
    )

@component
def AppMain():
    table_data = use_memo(lambda:get_sp500(rows=50))
    table = use_reactpy_table(Options(
        rows=table_data,
        cols = COLS
    ))

    return html.div(
        html.br(),
        html.h2('ReactPy Table Example'),
        html.table({"role": "grid"},
            THead(table),
            TBody(table.data.rows)
        ),
    )
```

[TanStack Table]: https://tanstack.com/table/latest
[ReactPy]: https://reactpy.dev/docs/index.html

