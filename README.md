# ChIter - iterator as a chain

Example:
```python
from chiter import ChIter as I


chain = I(range(100)) | I(range(100, 200)) | I(range(200, 300))
result = (chain
          .filter(lambda x: x % 2)
          .enumerate(start=1)
          .zip()
          .map(sum)
          .reduce(max))

assert result == 22500

```