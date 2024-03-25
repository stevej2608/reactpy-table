from typing import Callable
from pydantic import BaseModel

# pyright: reportReturnType=false

class PaginatorState(BaseModel):
    page_index: int
    page_size: int


PaginatorCallback = Callable[[PaginatorState], None]
