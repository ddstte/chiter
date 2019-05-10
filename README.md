# ChIter - iterable as a chain

Example:
```python
from chiter import ChIter as I


result = (I.from_iterables(range(100), range(100, 200), range(200, 300))
          .filter(lambda x: x % 2)
          .map(sum)
          .reduce(max))

assert result == 22500

```