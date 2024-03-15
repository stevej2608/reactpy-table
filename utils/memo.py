
from typing import Callable, Any, TypeVar, Tuple, Dict
from pydantic import BaseModel
from utils import log

TDeps = TypeVar('TDeps', bound=Tuple[Any, ...])
TMemoResult = TypeVar('TMemoResult')

class MemoOpts(BaseModel):
    name: str = 'Unknown'
    on_change: Callable[[Any], None] | None = None

NO_OPTS =  MemoOpts()

def memo(get_deps: Callable[[], TDeps],
         fn: Callable[..., TMemoResult],
         opts: MemoOpts = NO_OPTS) -> Callable[[], TMemoResult]:

    log.info('memo %s init', opts.name)

    deps: TDeps = [] # type: ignore
    result: TMemoResult = None # type: ignore

    def memoized_fn() -> TMemoResult:
        nonlocal deps, result

        log.info('memo %s get_deps', opts.name)

        new_deps = get_deps()
        deps_changed = len(new_deps) != len(deps) or any(dep != deps[i] for i, dep in enumerate(new_deps))

        if not deps_changed:
            log.info('memo %s - no change', opts.name)
            return result

        log.info('memo %s - update', opts.name)

        deps = new_deps
        result = fn(*new_deps)

        if opts.on_change:
            opts.on_change(result)

        return result

    return memoized_fn
