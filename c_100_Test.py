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



#def getthelength(x) -> tuple[int, int, int]:    
#    if x % 1 == 0:
#        total_length = full_numbers_length = len(str(x))
#    else:
#        total_length = len(str(x)) - 1
#        full_numbers_length, decimal_length = str(x).split(".")
#        full_numbers_length, decimal_length = len(full_numbers_length), len(decimal_length)
#        return total_length, full_numbers_length, decimal_length
#
#print(getthelength(100.1234)[0], getthelength(100.1234)[1], getthelength(100.1234)[2])
#


def getthelength(x) -> tuple[int, int, int]:    
    if x % 1 == 0:
        total_length = full_numbers_length = len(str(x))
        return total_length, full_numbers_length, 0
    else:
        total_length = len(str(x)) - 1
        full_numbers_length, decimal_length = str(x).split(".")
        full_numbers_length, decimal_length = len(full_numbers_length), len(decimal_length)
        return total_length, full_numbers_length, decimal_length
    
def is_length_under_9(x) -> bool:
    total_length, _, _ = getthelength(x)
    return total_length < 9


print(is_length_under_9(123456789))


print(f"{10.1:,.{1}f}")