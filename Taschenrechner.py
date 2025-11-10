def plus(x,y):
    Ergebnis = x + y
    return Ergebnis

def minus(x,y):
    Ergebnis = x - y
    return Ergebnis

def mal(x,y):
    Ergebnis = x * y
    return Ergebnis

def geteilt(x,y):
    Ergebnis = x / y
    return Ergebnis

x = int(input())
print("Die erste Zahk ist:", x)
y = int(input())
print("Die zweite Zahl ist:", y)



print("Für Addition tippe 'plus' für Subtraktion 'minus' für Multiplikation 'mal' und für Division 'geteilt'")
rechnug = str(input())

if rechnug == "plus":
    plusErgebnis = plus(x,y)
    print("Das Ergebnis ist:", plusErgebnis)

elif rechnug == "minus":
    minusErgebnis = minus(x,y)
    print("Das Ergebnis ist:", minusErgebnis)

elif rechnug == "mal":
    malErgebnis = mal(x,y)
    print("Das Ergebnis ist:", malErgebnis)

elif rechnug == "geteilt":
    geteiltErgebnis = geteilt(x,y)
    print("Das Ergebnis ist:", geteiltErgebnis)