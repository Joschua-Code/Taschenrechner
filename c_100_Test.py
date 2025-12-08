from decimal import Decimal

print(Decimal("10"))

q = 1.123456789

print(Decimal(f"{q:.4f}"))

x = 1233 / 2 * 2
länge_x = len(str(x))
print(len(str(x)))
print(f"hiii {str(x).split(".")}")


try:
    
    print(str(x)[6])

except IndexError:
    print("lol index mindex")
w = 3 / 2 * 2
print(f"w is {w} and len of w is {len(str(w))} and w converted to int is {int(w)} and the len of the int is {len(str(int(w)))}")

def test_if_number_is_short_enough(x):
    if x % 1 == 0:
        x = int(x)
        if len(str(x)) < 10:
            return True
        else:
            return False
        

print(test_if_number_is_short_enough(123456789))
print(len(str(1234567891)))

