# Python Practice

## Files

- `hello.py` - Basic Python hello world
- `typeandvalue.py` - Type and value examples (float, Decimal, math.pi)
- `05iteration.py` - Iteration examples
- `06String.py` - String operations
- `functiondome.py` - Function examples
- `slicing.py` - Slicing examples
- `test.py` - Test file
- `python_json.py` - JSON examples

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