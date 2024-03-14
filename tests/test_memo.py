from typing import Tuple
from utils.memo import ITest, memo



def test_memo_simple():

    class Example(ITest[int]):

        def __init__(self):

            self.computation = 0
            self.onchange_fired = 0

            self.pipeline = memo(
                self.get_deps,
                self.expensive_computation,
                {'onChange': self.on_change}
                )

        def get_deps(self) -> Tuple[int, int]:
            return (1, 2)

        def expensive_computation(self, a: int, b: int) -> int:
            self.computation +=1
            return a + b

        def on_change(self, result: int):
            self.onchange_fired += 1

    ex = Example()

    # First pass

    res = ex.pipeline()
    assert res == 3
    assert ex.computation == 1
    assert ex.onchange_fired == 1

    # Second pass, nothing changes

    res = ex.pipeline()
    assert res == 3
    assert ex.computation == 1
    assert ex.onchange_fired == 1
