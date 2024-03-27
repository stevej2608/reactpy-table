from typing import Callable
from pydantic import BaseModel
import json

# pyright: reportReturnType=false

class SortState(BaseModel):
    id: str
    desc: str

    def __str__(self):
        return f"{json.dumps(self.model_dump())}"


SortCallback = Callable[[SortState], None]
