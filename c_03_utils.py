from decimal import Decimal
import os, sys

def as_decimal(x):
    if isinstance(x, Decimal):
        return x
    if isinstance(x, float):
        return Decimal(str(x))
    if isinstance(x, (int, str)):
        return Decimal(x)
    raise TypeError(f"Unsupported type: {type(x).__name__}")

# Fix for pyinstaller to get the icon into the exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)