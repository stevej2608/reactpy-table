## reactpy-table

![](https://raw.githubusercontent.com/stevej2608/reactpy-table/master/docs/img/screenshot.png)

Headless UI for building powerful tables with [ReactPy]. The project 
takes its design ideas from the hugely popular, ReactJS based, [TanStack Table].

The initial release supports the following features:

- [X] Headless UI, CSS agnostic
- [X] Freeform text search
- [X] Forward/Reverse column based sort
- [X] Pagination
- [X] Integration with SQLModel/SQLAlchemy (full text search, sort and pagination)
- [ ] Integration with Pandas (in progress)
- [ ] Remote large dataset support (in progress)

## Usage

	pip install reactpy-table

*[basic_example.py](examples/basic_example.py)*
```python
from reactpy import component, html, use_memo
from reactpy_table import Options, Table, use_reactpy_table

from .data.sp500 import COLS, CompanyModel, get_sp500

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

```

### More complex examples

**examples/table_example.py** demonstrates search, sort and pagination on SP500 
companies table. The built-in feature data pipeline is used.

**examples/books/books_example.py** demonstrates search, sort and pagination on
a SQLite book database containing 100k books. Search, sort and 
pagination is handled by SQL queries.

* Full text search on database < 20ms
* Page traversal < 2ms


## Feature Set

The row data presented to the user for display is pre-processed by a
data-pipeline of table features:

    1. Search, filters the initial usr data
    2. Sort, the search result by column (up/down)
    3. Paginate, the sort result (if enabled)
    4. RowOps, CRUD operations on the data

Each feature presents an API to the user that directs its
operation. Any change will, if required, recalculate the table data.

A default set of features is applied by default. One or more custom
features that will replace the default can be supplied as options 
when the table is created.

A callback mechanism is available for each feature that provides
support for accessing external data sources (databases, 
pandas data-frames etc).


### Custom Features

All features are instantiated using a strict pattern. As
an example a custom paginator that accepts *page _size* and
*start_page* would be created as follows:

```
def getCustomPaginator(page_size, start_page) 

    def _feature_factory(table, updater):
        return CustomPaginator(table, updater, page_size, start_page)
    
    return _feature_factory

```
The custom feature is passed as an option when the table is created:
```
table = use_reactpy_table(Options(
    ...
    paginator = getCustomPaginator(page_size=100, start_page=25)
))
```

The table initialization logic calls *_feature_factory(table, updater)* to
supply reactpy's internal *table* and *updater* to the custom factory.


[TanStack Table]: https://tanstack.com/table/latest
[ReactPy]: https://reactpy.dev/docs/index.html

