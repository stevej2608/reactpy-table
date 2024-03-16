
from typing import Callable, Any, TypeVar, Tuple
from pydantic import BaseModel
from utils import log

TDeps = TypeVar('TDeps', bound=Tuple[Any, ...])
TMemoResult = TypeVar('TMemoResult')

class MemoOpts(BaseModel):
    name: str = 'Unknown'
    debug: bool = False
    on_change: Callable[[Any], None] | None = None

NO_OPTS =  MemoOpts()

def memo(get_deps: Callable[[], TDeps],
         fn: Callable[..., TMemoResult],
         opts: MemoOpts = NO_OPTS) -> Callable[[], TMemoResult]:
    
    if opts.debug:
        log.info('memo %s init', opts.name)

    deps: TDeps = () # type: ignore
    result: TMemoResult = None # type: ignore

    def memoized_fn() -> TMemoResult:
        nonlocal deps, result

        if opts.debug:
            log.info('memo %s old deps %s', opts.name, deps)

        new_deps = get_deps()
        deps_changed = len(new_deps) != len(deps) or any(dep != deps[i] for i, dep in enumerate(new_deps))

        if opts.debug:
            log.info('memo %s new deps %s (changed=%s)', opts.name, new_deps, deps_changed)
            assert True

        if not deps_changed:
            return result

        deps = new_deps
        result = fn(*new_deps)

        if opts.on_change:
            opts.on_change(result)

        return result

    return memoized_fn
