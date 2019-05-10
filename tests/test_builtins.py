from functools import reduce
from operator import add

from chiter import ChIter


def test_filter():
    i = ChIter(range(5)).filter(lambda x: x > 2)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(3, 5))


def test_map():
    i = ChIter(range(5)).map(lambda x: x + 1)

    assert isinstance(i, ChIter)
    assert list(i) == list(range(1, 6))


def test_enumerate():
    i = ChIter(range(5)).enumerate()

    assert isinstance(i, ChIter)
    assert list(i) == list(enumerate(range(5)))


def test_enumerate_start():
    i = ChIter(range(5)).enumerate(start=2)

    assert isinstance(i, ChIter)
    assert list(i) == list(enumerate(range(5), start=2))


def test_zip():
    i = ChIter(enumerate(range(5))).zip()

    assert isinstance(i, ChIter)
    assert list(i) == list(zip(*enumerate(range(5))))


def test_reduce():
    i = ChIter(range(5)).reduce(add)

    assert isinstance(i, int)
    assert i == reduce(add, range(5))


def test_reduce_initial():
    i = ChIter(range(5)).reduce(add, initial=2)

    assert isinstance(i, int)
    assert i == reduce(add, range(5), 2)


def test_sorted():
    i = ChIter(range(5)).sorted()

    assert isinstance(i, ChIter)
    assert list(i) == sorted(range(5))


def test_sorted_key():
    i = ChIter(range(5)).sorted(key=lambda x: -x)

    assert isinstance(i, ChIter)
    assert list(i) == sorted(range(5), key=lambda x: -x)


def test_sorted_key_reverse():
    i = ChIter(range(5)).sorted(key=lambda x: -x, reverse=True)

    assert isinstance(i, ChIter)
    assert list(i) == sorted(range(5), key=lambda x: -x, reverse=True)


def test_reversed():
    i = ChIter(range(5)).reversed()

    assert isinstance(i, ChIter)
    assert list(i) == list(reversed(range(5)))


def test_all_true():
    result = ChIter(range(1, 2)).all()

    assert isinstance(result, bool)
    assert result is True


def test_all_false():
    result = ChIter(range(2)).all()

    assert isinstance(result, bool)
    assert result is False


def test_any_true():
    result = ChIter(range(2)).any()

    assert isinstance(result, bool)
    assert result is True


def test_any_false():
    result = ChIter(range(1)).any()

    assert isinstance(result, bool)
    assert result is False


def test_set():
    i = ChIter(range(5)).set()

    assert isinstance(i, set)
    assert set(range(5)) == i


def test_frozenset():
    i = ChIter(range(5)).frozenset()

    assert isinstance(i, frozenset)
    assert frozenset(range(5)) == i


def test_list():
    i = ChIter(range(5)).list()

    assert isinstance(i, list)
    assert list(range(5)) == i


def test_tuple():
    i = ChIter(range(5)).tuple()

    assert isinstance(i, tuple)
    assert tuple(range(5)) == i


def test_dict():
    items = [(1, 2), (3, 4)]

    i = ChIter(items).dict()

    assert isinstance(i, dict)
    assert dict(items) == i
