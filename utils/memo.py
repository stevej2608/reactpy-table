
from typing import Callable, Any, TypeVar, Tuple, Dict, Protocol, Generic

T = TypeVar('T')
TDeps = TypeVar('TDeps', bound=Tuple[Any, ...])
TResult = TypeVar('TResult')

# class TMemo(Protocol):
#     def __call__(self, get_deps: Callable[[], TDeps],
#          fn: Callable[..., TResult],
#          opts: Dict[str, Any] | None = None) -> Callable[[], TResult]: ...

T = TypeVar('T')

class IPipeline(Protocol, Generic[T]):
    pipeline: Callable[[], T]


def memo(get_deps: Callable[[], TDeps],
         fn: Callable[..., TResult],
         opts: Dict[str, Any] | None = None) -> Callable[[], TResult]:


    deps: TDeps = [] # type: ignore
    result: TResult = None # type: ignore

    def memoized_fn() -> TResult:
        nonlocal deps, result

        new_deps = get_deps()
        deps_changed = len(new_deps) != len(deps) or any(dep != deps[i] for i, dep in enumerate(new_deps))

        if not deps_changed:
            return result

        print('memo: DEPS CHANGED')

        deps = new_deps
        result = fn(*new_deps)

        if opts is not None and 'onChange' in opts:
            opts['onChange'](result)

        return result

    return memoized_fn



def get_deps() -> Tuple[int, int]:
    return (1, 2)

def expensive_computation(a: int, b: int) -> int:
    print("Performing expensive computation...")
    return a + b

def on_change(result: int):
    print(f"Result changed: {result}")

memoized_fn = memo(get_deps, expensive_computation, {'onChange': on_change})


class ITest(Protocol, Generic[T]):

    pipeline: Callable[[], T]

class Test(ITest[int]):

    def __init__(self):
        self.pipeline = memo(
            self.get_deps,
            self.expensive_computation,
            {'onChange': self.on_change}
            )

    def get_deps(self) -> Tuple[int, int]:
        return (1, 2)

    def expensive_computation(self, a: int, b: int) -> int:
        print("Performing expensive computation...")
        return a + b

    def on_change(self, result: int):
        print(f"Result changed: {result}")