
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
    """Keeps an internal state. If the new state, returned by get_deps()
    is different the, costly, update method fn is called. The returned
    value and the new state are saved internally

    Args:
        get_deps (Callable[[], TDeps]): Dependencies that, on change, update the memo
        fn (Callable[..., TMemoResult]): The update function that is called to update the saved value
        opts (MemoOpts, optional): Options, Defaults to NO_OPTS.

    Returns:
        Callable[[], TMemoResult]: _description_
    """

    if opts.debug:
        log.info('%s init', opts.name)

    # Saved state

    deps: TDeps = tuple([None]) # type: ignore
    result: TMemoResult = None # type: ignore

    def memoized_fn() -> TMemoResult:
        nonlocal deps, result

        if opts.debug:
            log.info('%s get deps old=%s >>>', opts.name, deps)

        new_deps = get_deps()
        deps_changed = len(new_deps) != len(deps) or any(dep != deps[i] for i, dep in enumerate(new_deps))


        if not deps_changed:

            if opts.debug:
                log.info('%s no change <<<', opts.name)

            return result

        deps = new_deps
        result = fn(*new_deps)

        if opts.on_change:
            opts.on_change(result)

        if opts.debug:
            log.info('%s change new=%s <<<', opts.name, result)

        return result

    return memoized_fn
