from functools import partial

from chiter import Pipeline


def test_pipeline():
    pipeline = Pipeline(partial(filter, None), partial(map, str), list, "".join)

    assert "12" == pipeline(range(3))


def test_combine_pipelines():
    to_upper_string = Pipeline(partial(map, str), partial(map, str.upper), "".join)
    pipeline_two = Pipeline(partial(filter, None), to_upper_string)

    assert "PIPE" == pipeline_two(["P", 0, "I", 0, "P", 0, "E"])
