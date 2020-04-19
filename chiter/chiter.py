from __future__ import annotations

import itertools
import operator
from functools import reduce, partial
from typing import Any, Callable, Optional, Iterable, Iterator, Set, FrozenSet, List, Tuple, Dict

from .pipeline import Pipeline


class ChIter(Iterator[Any]):
    __slots__ = ("_iterable", "_length_hint", "_strategy")

    @classmethod
    def from_iterables(cls, *iterables) -> ChIter:
        obj = cls(itertools.chain(*iterables))
        obj._length_hint = sum(map(operator.length_hint, iterables))
        return obj

    def __init__(self, iterable: Iterable):
        self._length_hint = operator.length_hint(iterable)
        self._iterable = iter(iterable)
        self._strategy = []

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self._strategy:
            self._iterable = iter(Pipeline(*self._strategy)(self._iterable))
            self._strategy = []

        if self._length_hint:
            self._length_hint -= 1

        return next(self._iterable)

    def __add__(self, other) -> ChIter:
        if not hasattr(other, "__iter__"):
            return NotImplemented
        return type(self).from_iterables(self, other)

    def __radd__(self, other) -> ChIter:
        if not hasattr(other, "__iter__"):
            return NotImplemented
        return type(self).from_iterables(other, self)

    def __length_hint__(self) -> int:
        return self._length_hint

    def filter(self, func: Optional[Callable]) -> ChIter:
        self._strategy.append(partial(filter, func))
        return self

    def map(self, func: Callable) -> ChIter:
        self._strategy.append(partial(map, func))
        return self

    def enumerate(self, start: int = 0) -> ChIter:
        self._strategy.append(lambda x: enumerate(x, start=start))
        return self

    def zip(self) -> ChIter:
        self._strategy.append(lambda x: zip(*x))
        return self

    def reduce(self, function: Callable, initial=None) -> Any:
        args = (i for i in (self, initial) if i is not None)
        return reduce(function, *args)

    def sorted(self, key: Optional[Callable] = None, reverse: bool = False) -> ChIter:
        self._strategy.append(lambda x: sorted(x, key=key, reverse=reverse))
        return self

    def reversed(self) -> ChIter:
        self._strategy.append(tuple)
        self._strategy.append(reversed)
        return self

    def sum(self, start=0) -> int:
        return sum(self, start)

    def all(self) -> bool:
        return all(self)

    def any(self) -> bool:
        return any(self)

    def set(self) -> Set[Any]:
        return set(self)

    def frozenset(self) -> FrozenSet[Any]:
        return frozenset(self)

    def list(self) -> List[Any]:
        return list(self)

    def tuple(self) -> Tuple[Any]:
        return tuple(self)

    def dict(self) -> Dict[Any, Any]:
        return dict(self)

    def accumulate(self, func=operator.add) -> ChIter:
        self._strategy.append(lambda x: itertools.accumulate(x, func))
        return self

    def combinations(self, r: int) -> ChIter:
        self._strategy.append(lambda x: itertools.combinations(x, r))
        return self

    def combinations_with_replacement(self, r: int) -> ChIter:
        self._strategy.append(lambda x: itertools.combinations_with_replacement(x, r))
        return self

    def compress(self, selectors: Iterable[bool]) -> ChIter:
        self._strategy.append(lambda x: itertools.compress(x, selectors))
        return self

    def dropwhile(self, predicate: Callable) -> ChIter:
        self._strategy.append(partial(itertools.dropwhile, predicate))
        return self

    def groupby(self, key: Optional[Callable] = None) -> ChIter:
        self._strategy.append(lambda x: itertools.groupby(x, key=key))
        return self

    def filterfalse(self, predicate: Callable) -> ChIter:
        self._strategy.append(partial(itertools.filterfalse, predicate))
        return self

    def slice(self, start: int, stop: Optional[int] = None, step: Optional[int] = None) -> ChIter:
        args = (start, stop, step)
        start_is_stop = all((i is None for i in args[1:]))
        slice_args = args[:1] if start_is_stop else args

        self._strategy.append(lambda x: itertools.islice(x, *slice_args))
        return self

    def permutations(self, r: Optional[int] = None) -> ChIter:
        self._strategy.append(lambda x: itertools.permutations(x, r))
        return self

    def product(self, *, repeat=1) -> ChIter:
        self._strategy.append(lambda x: itertools.product(x, repeat=repeat))
        return self

    def takewhile(self, func=Callable) -> ChIter:
        self._strategy.append(partial(itertools.takewhile, func))
        return self

    def starmap(self, func: Callable) -> ChIter:
        self._strategy.append(partial(itertools.starmap, func))
        return self

    def tee(self, n: int = 2) -> ChIter:
        self._strategy.append(lambda x: map(type(self), itertools.tee(x, n)))
        return self

    def cycle(self) -> ChIter:
        self._strategy.append(itertools.cycle)
        return self

    def zip_longest(self, *, fillvalue=None) -> ChIter:
        self._strategy.append(lambda x: itertools.zip_longest(*x, fillvalue=fillvalue))
        return self

    def flat(self) -> ChIter:
        self._strategy.append(itertools.chain.from_iterable)
        return self
