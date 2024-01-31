from typing import List, Dict, Type
from random import randint, seed
from pydantic import BaseModel

SEED = 19414882697304228148394


def make_data(number:int, seed_data:List[Dict], model: Type[BaseModel], random_seed=SEED):
    result = []
    index = 1

    seed(random_seed)

    print([randint(1, 10) for _ in range(5)])

    while number:
        data = seed_data[randint(0, len(seed_data) - 1)]
        data['index'] = index
        result.append(model(**data))
        number -= 1
        index += 1
    return result
