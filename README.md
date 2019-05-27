# ChIter - iterable as a chain

## Why?
Chains do not require saving the intermediate state in temporary variables and look more readable.

### Examples
Get the sum of all the numbers from some data: 
```python
data = "23,45,67\n45,56,55\n\n45,a,5\n-45,56,0"
```

#### first way

```python
from itertools import chain


chunks = (chunk.split(',') for chunk in data.split())
flat_data = chain.from_iterable(chunks)
items = (int(item) for item in flat_data if not item.isalpha())
result = sum(items)

assert result == 352
```
#### second way
```python
from itertools import chain


result = sum((
    int(item)
    for item in chain.from_iterable(map(lambda c: c.split(','), data.split()))
    if not item.isalpha()
))
assert result == 352
```
#### chiter way
```python
from chiter import ChIter as I


result = (I(data.split())
          .map(lambda x: x.split(','))
          .flat()
          .filterfalse(str.isalpha)
          .map(int)
          .sum())

assert result == 352
```

## Requirements
* Python 3.7+

## Related Libraries
* [flupy](https://github.com/olirice/flupy)