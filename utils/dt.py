from typing import Optional, Protocol
import time

class DTCallback(Protocol):
    def __call__(self, reset: Optional[bool] = None) -> str: ...


def DT() -> DTCallback:
    """Code execution timer

    Returns:
        Callable[..., str]: Returns log function that when called returns the elapsed milliseconds

    Usage:

        dt = DT()

        <SOME CODE>

        print(f"Code took {dt(reset=True)} ms")

        <SOME MORE CODE>

        print(f"More code took {dt(reset=True)} ms")
    """

    start_time = time.time()

    def log(reset:Optional[bool]=None) -> str:
        nonlocal start_time
        end_time = time.time()
        dt = (end_time - start_time) * 1000
        if reset is None or reset is True:
            start_time = end_time
        return "%.3f" % dt


    return log


# python -m examples.books.db2

if __name__ == "__main__":
    dt = DT()

    print(f" {dt()} ms")
