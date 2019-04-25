from __future__ import annotations

import itertools
from functools import reduce
from operator import length_hint, add
from typing import Any, Callable, Optional, Iterable, Iterator

from .meta import ChIterMeta


class ChIter(Iterator[Any], metaclass=ChIterMeta):
    __slots__ = ('_iterable', '_length_hint')

    def __init__(self, iterable: Iterable):
        self._length_hint = length_hint(iterable)
        self._iterable = iter(iterable)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        return next(self._iterable)

    def __add__(self, other) -> ChIter:
        if not hasattr(other, '__iter__'):
            return NotImplemented
        return itertools.chain(self, type(self)(other))

    def __radd__(self, other) -> ChIter:
        if not hasattr(other, '__iter__'):
            return NotImplemented
        return itertools.chain(type(self)(other), self)

    __or__ = __add__
    __ror__ = __radd__

    def __length_hint__(self) -> int:
        return self._length_hint

    def filter(self, func: Optional[Callable]) -> ChIter:
        return filter(func, self)

    def map(self, func: Callable) -> ChIter:
        return map(func, self)

    def enumerate(self, start: int = 0) -> ChIter:
        return enumerate(self, start=start)

    def zip(self) -> ChIter:
        return zip(*self)

    def reduce(self, func: Callable, initial=None) -> Any:
        args = (i for i in (self, initial) if i is not None)
        return reduce(func, *args)

    def sorted(self, key: Optional[Callable] = None, reverse: bool = False) -> ChIter:
        return sorted(self, key=key, reverse=reverse)

    def reversed(self) -> ChIter:
        return reversed(tuple(self))

    def accumulate(self, func=add) -> ChIter:
        return itertools.accumulate(self, func)

    def flatten(self) -> ChIter:
        return itertools.chain.from_iterable(self)
