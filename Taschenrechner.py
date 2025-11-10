def plus(x,y):
    ergebnis = x + y
    return ergebnis

def minus(x,y):
    ergebnis = x - y
    return ergebnis

def mal(x,y):
    ergebnis = x * y
    return ergebnis

def geteilt(x,y):
    ergebnis = x / y
    return ergebnis

x = int(input())
print("Die erste Zahk ist:", x)
y = int(input())
print("Die zweite Zahl ist:", y)



print("Für Addition tippe 'plus' für Subtraktion 'minus' für Multiplikation 'mal' und für Division 'geteilt'")
rechnug = str(input())

if rechnug == "plus":
    plus_ergebnis = plus(x,y)
    print("Das Ergebnis ist:", plus_ergebnis)

elif rechnug == "minus":
    minus_ergebnis = minus(x,y)
    print("Das Ergebnis ist:", minus_ergebnis)

elif rechnug == "mal":
    mal_ergebnis = mal(x,y)
    print("Das Ergebnis ist:", mal_ergebnis)

elif rechnug == "geteilt":
    geteilt_ergebnis = geteilt(x,y)
    print("Das Ergebnis ist:", geteilt_ergebnis)