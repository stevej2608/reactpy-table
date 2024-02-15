from typing import List, Dict, Type, TypeVar, Any, cast
from random import randint, seed
from pydantic import BaseModel

SEED = 19414882697304228148394


T = TypeVar('T', bound=BaseModel)

def make_data(number:int, seed_data:List[T], model: Type[BaseModel], random_seed: int=SEED) -> List[T]:
    result: List[T] = []
    index = 1

    seed(random_seed)

    print([randint(1, 10) for _ in range(5)])

    while number:
        data: Dict[str, Any] = seed_data[randint(0, len(seed_data) - 1)].model_dump()
        data['index'] = index
        result.append(cast(T, model(**data)))
        number -= 1
        index += 1
    return result
