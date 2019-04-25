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


def test_next_empty():
    with pytest.raises(StopIteration):
        next(ChIter([]))


def test_add():
    i = ChIter(range(5)) + ChIter(range(5, 10))

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_add_left():
    i = ChIter(range(5)) + range(5, 10)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_add_left_not_iter():
    with pytest.raises(TypeError):
        ChIter(range(5)) + None


def test_add_right():
    i = range(5) + ChIter(range(5, 10))

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_add_right_not_iter():
    with pytest.raises(TypeError):
        None + ChIter(range(5, 10))


def test_or_left():
    i = ChIter(range(5)) | range(5, 10)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_or_left_not_iter():
    with pytest.raises(TypeError):
        ChIter(range(5)) | None


def test_or_right():
    i = range(5) | ChIter(range(5, 10))

    assert isinstance(i, ChIter)
    assert list(i) == list(range(10))


def test_or_right_not_iter():
    with pytest.raises(TypeError):
        None | ChIter(range(5, 10))


def test_length_hint():
    i = length_hint(ChIter(range(5)))

    assert isinstance(i, int)
    assert i == length_hint(range(5))
