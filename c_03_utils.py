from decimal import Decimal

def as_decimal(x):
    if isinstance(x, Decimal):
        return x
    if isinstance(x, float):
        return Decimal(str(x))
    if isinstance(x, (int, str)):
        return Decimal(x)
    raise TypeError(f"Unsupported type: {type(x).__name__}")