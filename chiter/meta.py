from abc import ABCMeta
from functools import wraps

from .helpers import is_chiter


class ChIterMeta(ABCMeta):
    def __new__(mcs, name, bases, defaults):
        cls = super().__new__(mcs, name, bases, defaults)
        iterables = {k: v for k, v in defaults.items() if is_chiter(cls, v)}

        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                return result if result is NotImplemented else cls(result)

            return inner

        for name, f in iterables.items():
            setattr(cls, name, wrapper(f))
        return cls
