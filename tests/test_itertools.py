import itertools

from chiter import ChIter


def test_accumulate():
    i = ChIter(range(5)).accumulate()

    assert isinstance(i, ChIter)
    assert list(i) == list(itertools.accumulate(range(5)))


def test_flatten():
    i = ChIter(enumerate(range(5))).flatten()

    assert isinstance(i, ChIter)
    assert list(i) == list(itertools.chain.from_iterable(enumerate(range(5))))


def test_tee():
    i = ChIter(range(5)).tee()

    assert isinstance(i, ChIter)
    i1, i2 = i

    assert isinstance(i1, ChIter)
    assert isinstance(i2, ChIter)

    assert list(i1) == list(i2)


def test_tee_n():
    i = ChIter(range(5)).tee(3)

    assert isinstance(i, ChIter)
    i1, i2, i3 = i

    assert isinstance(i1, ChIter)
    assert isinstance(i2, ChIter)
    assert isinstance(i3, ChIter)

    assert list(i1) == list(i2) == list(i3)


def test_cycle():
    i = ChIter([None]).cycle()

    assert isinstance(i, ChIter)
    assert list(zip(i, range(5))) == list(zip(itertools.cycle([None]), range(5)))


def test_combinations():
    i = ChIter(range(5)).combinations(2)

    assert isinstance(i, ChIter)
    assert list(itertools.combinations(range(5), 2)) == list(i)


def test_combinations_with_replacement():
    i = ChIter(range(5)).combinations_with_replacement(2)

    assert isinstance(i, ChIter)
    assert list(itertools.combinations_with_replacement(range(5), 2)) == list(i)


def test_compress():
    selectors = [True, False, True]
    i = ChIter(range(5)).compress(selectors)

    assert isinstance(i, ChIter)
    assert list(itertools.compress(range(5), selectors)) == list(i)


def test_dropwhile():
    def func(x):
        return x > 2

    i = ChIter(range(5)).dropwhile(func)

    assert isinstance(i, ChIter)
    assert list(itertools.dropwhile(func, range(5))) == list(i)


def test_filterfalse():
    def func(x):
        return x % 2

    i = ChIter(range(5)).filterfalse(func)

    assert isinstance(i, ChIter)
    assert list(itertools.filterfalse(func, range(5))) == list(i)


def test_groupby():
    iterable = [1, 1, 3, 2, 2]

    i = ChIter(iterable).groupby()

    assert isinstance(i, ChIter)
    assert [(k, list(g)) for k, g in itertools.groupby(iterable)] == [(k, list(g)) for k, g in i]


def test_groupby_key():
    def key(x):
        return x % 2

    iterable = [1, 1, 3, 2, 2]

    i = ChIter(iterable).groupby(key)

    assert isinstance(i, ChIter)
    assert [(k, list(g)) for k, g in itertools.groupby(iterable, key)] == [(k, list(g)) for k, g in i]


def test_slice():
    i = ChIter(range(5)).slice(2)

    assert isinstance(i, ChIter)
    assert list(itertools.islice(range(5), 2)) == list(i)


def test_slice_kwargs():
    i = ChIter(range(5)).slice(start=1, stop=4, step=2)

    assert isinstance(i, ChIter)
    assert list(itertools.islice(range(5), 1, 4, 2)) == list(i)


def test_permutations():
    i = ChIter(range(5)).permutations()

    assert isinstance(i, ChIter)
    assert list(itertools.permutations(range(5))) == list(i)


def test_permutations_repeat():
    i = ChIter(range(5)).permutations(2)

    assert isinstance(i, ChIter)
    assert list(itertools.permutations(range(5), 2)) == list(i)


def test_product():
    i = ChIter(range(5)).product()

    assert isinstance(i, ChIter)
    assert list(itertools.product(range(5))) == list(i)


def test_product_repeat():
    i = ChIter(range(5)).product(repeat=2)

    assert isinstance(i, ChIter)
    assert list(itertools.product(range(5), repeat=2)) == list(i)


def test_starmap():
    i = ChIter(enumerate(range(5))).starmap(pow)

    assert isinstance(i, ChIter)
    assert list(itertools.starmap(pow, enumerate(range(5)))) == list(i)


def test_takewhile():
    def predicate(x):
        return x <= 2

    i = ChIter(range(5)).takewhile(predicate)

    assert isinstance(i, ChIter)
    assert list(itertools.takewhile(predicate, range(5))) == list(i)


def test_zip_longest():
    i = ChIter(enumerate(range(5))).zip_longest()

    assert isinstance(i, ChIter)
    assert list(itertools.zip_longest(*enumerate(range(5)))) == list(i)


def test_zip_longest_fillvalue():
    data = [(1, 2), (1,)]
    empty_value = object()

    i = ChIter(data).zip_longest(fillvalue=empty_value)

    assert isinstance(i, ChIter)
    assert list(itertools.zip_longest(*data, fillvalue=empty_value)) == list(i)
