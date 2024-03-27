from typing import Callable, Literal
import json
from pydantic import BaseModel

# pyright: reportReturnType=false

SQL_DIRECTION = Literal['ASC', 'DESC']

class SortState(BaseModel):
    id: str
    desc: SQL_DIRECTION

    def __str__(self):
        return f"{json.dumps(self.model_dump())}"


SortCallback = Callable[[SortState], None]
