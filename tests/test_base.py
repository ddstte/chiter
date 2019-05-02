from collections.abc import Iterator
from operator import length_hint

import pytest

from chiter import ChIter


def test_as_iterator():
    assert isinstance(ChIter([]), Iterator)


def test_iterator():
    iterator = iter(ChIter([]))
    assert isinstance(iterator, Iterator)


def test_next():
    item = next(ChIter([None]))
    assert item is None


def test_next_with_length_hint():
    i = ChIter([None])

    assert length_hint(i) == 1
    next(i)
    assert length_hint(i) == 0


def test_next_empty():
    with pytest.raises(StopIteration):
        next(ChIter([]))


def test_add():
    i = ChIter(range(5)) + ChIter(range(5, 10))

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_add_with_length_hint():
    one = ChIter(range(5))
    two = ChIter(range(5, 10))
    i = one + two
    length = length_hint(one) + length_hint(two)

    assert length_hint(i) == length


def test_add_left():
    i = ChIter(range(5)) + range(5, 10)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_add_left_with_length_hint():
    one = ChIter(range(5))
    two = range(5, 10)
    i = one + two
    length = length_hint(one) + length_hint(two)

    assert length_hint(i) == length


def test_add_left_not_iter():
    with pytest.raises(TypeError):
        ChIter(range(5)) + None


def test_add_right():
    i = range(5) + ChIter(range(5, 10))

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_add_right_with_length_hint():
    one = range(5, 10)
    two = ChIter(range(5))
    i = one + two
    length = length_hint(one) + length_hint(two)

    assert length_hint(i) == length


def test_add_right_not_iter():
    with pytest.raises(TypeError):
        None + ChIter(range(5, 10))


def test_length_hint():
    i = length_hint(ChIter(range(5)))

    assert isinstance(i, int)
    assert i == length_hint(range(5))


def test_from_iterables():
    i = ChIter.from_iterables(range(5), range(5, 10))

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_from_iterables_with_length_hint():
    i = ChIter.from_iterables(range(5), range(5, 10))

    assert length_hint(i) == length_hint(range(10))
