
from typing import Callable, Any, TypeVar, Tuple, Dict, Protocol, Generic

T = TypeVar('T')
TDeps = TypeVar('TDeps', bound=Tuple[Any, ...])
TResult = TypeVar('TResult')


class ITest(Protocol, Generic[T]):
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
