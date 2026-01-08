from decimal import Decimal

def test1():
    x = 10
    x = test0()
    return x


def test0():
    x = 11
    return 11


print(test1())