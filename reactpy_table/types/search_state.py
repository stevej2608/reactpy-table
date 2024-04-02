import json
from typing import Callable

from pydantic import BaseModel



class SearchState(BaseModel):
    search_term: str = ''
    case_sensitive: bool = False

    def __str__(self):
        return f"{json.dumps(self.model_dump())}"


SearchCallback = Callable[[SearchState], None]
