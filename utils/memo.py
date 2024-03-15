
from typing import Callable, Any, TypeVar, Tuple, Dict

TDeps = TypeVar('TDeps', bound=Tuple[Any, ...])
TMemoResult = TypeVar('TMemoResult')


def memo(get_deps: Callable[[], TDeps],
         fn: Callable[..., TMemoResult],
         opts: Dict[str, Any] | None = None) -> Callable[[], TMemoResult]:


    deps: TDeps = [] # type: ignore
    result: TMemoResult = None # type: ignore

    def memoized_fn() -> TMemoResult:
        nonlocal deps, result

        new_deps = get_deps()
        deps_changed = len(new_deps) != len(deps) or any(dep != deps[i] for i, dep in enumerate(new_deps))

        if not deps_changed:
            return result

        deps = new_deps
        result = fn(*new_deps)

        if opts is not None and 'onChange' in opts:
            opts['onChange'](result)

        return result

    return memoized_fn
