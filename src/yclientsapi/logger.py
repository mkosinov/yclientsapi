import functools
import inspect
from collections.abc import Callable
from typing import TypeVar, cast

F = TypeVar("F", bound=Callable)


def log_call(func: F) -> F:  # noqa: UP047, RUF100
    """
    Decorator to log the calling of API methods using self.__api.logger.
    Logs method name and arguments (excluding self).
    Preserves the type signature of the decorated function.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        logger = getattr(getattr(self, "__api", None), "logger", None)
        if logger:
            sig = inspect.signature(func)
            bound = sig.bind(self, *args, **kwargs)
            bound.apply_defaults()
            args_repr = []
            for name, value in list(bound.arguments.items())[1:]:
                if name.lower() in {"password", "token", "user_token", "partner_token"}:
                    value = "***"
                args_repr.append(f"{name}={value!r}")
            logger.debug(f"Calling {func.__qualname__}({', '.join(args_repr)})")
        return func(self, *args, **kwargs)

    return cast("F", wrapper)
