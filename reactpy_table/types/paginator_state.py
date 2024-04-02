import json
from typing import Callable

from pydantic import BaseModel

class PaginatorState(BaseModel):
    page_index: int
    page_size: int

    @property
    def skip(self):
        return self.page_size * self.page_index
    
    @property
    def limit(self):
        return self.page_size


    def __str__(self):
        return f"{json.dumps(self.model_dump())}"


PaginatorCallback = Callable[[PaginatorState], None]
