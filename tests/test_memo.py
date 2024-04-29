from typing import Tuple, Generic, Protocol, Callable
from reactpy_table.utils.memo import TMemoResult, memo, MemoOpts



def test_memo_simple():

    class IPipeline(Protocol, Generic[TMemoResult]):
        pipeline: Callable[[], TMemoResult]

    class Example(IPipeline[int]):

        def __init__(self):

            self.computation = 0
            self.onchange_fired = 0

            self.pipeline = memo(
                self.get_deps,
                self.expensive_computation,
                MemoOpts(on_change=self.on_change)
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
