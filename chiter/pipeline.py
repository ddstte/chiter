import functools
import reprlib


class Pipeline:
    def __init__(self, *functions):
        self._functions = functions

    def __call__(self, value):
        return functools.reduce(lambda acc, func: func(acc), self._functions, value)

    def __repr__(self):
        return f"<Pipeline {reprlib.repr(self._functions)}>"
