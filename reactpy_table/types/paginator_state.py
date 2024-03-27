import json
from typing import Callable

from pydantic import BaseModel

# pyright: reportReturnType=false

class PaginatorState(BaseModel):
    page_index: int
    page_size: int

    def __str__(self):
        return f"{json.dumps(self.model_dump())}"


PaginatorCallback = Callable[[PaginatorState], None]
