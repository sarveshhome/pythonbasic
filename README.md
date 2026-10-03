# Python Practice

## Files

- `hello.py` - Prints "Hello World"
- `typeandvalue.py` - Type/value examples: float vs `Decimal`, `math.pi`, conditional comparisons, temperature conversion, `random`
- `05iteration.py` - Loops and iteration: `while`, `for`, and a `min_method` function
- `06String.py` - String operations: indexing, slicing, `endswith`, string comparison
- `functiondome.py` - Function examples: `print_lyrics`, `repeat_lyrics`, `print_twice`, `addtwo`
- `slicing.py` - Practice mix: string formatting, integer division, lists, loops, math functions, web scraping with BeautifulSoup
- `test.py` - Duplicate of `slicing.py` (same exercises)
- `python_json.py` - Parse a JSON string into a Python dictionary

## Quick Examples

### Print type of pi
```python
import math
print(type(math.pi))  # <class 'float'>
```

### Float vs Decimal
```python
from decimal import Decimal

f = 3.14
d = Decimal("3.14")

print(type(f), f)  # <class 'float'> 3.14
print(type(d), d)  # <class 'decimal.Decimal'> 3.14
```

### JSON parsing
```python
import json

x = '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])  # 30
```
