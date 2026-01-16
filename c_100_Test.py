from decimal import Decimal




#es muss mindestens auf 2 nachkommastellen gerundet werden ansonsten kommt Fehlerfenster
#Fehlerfenster hat aberauch das Ergebnis

#hilfsfunktion für result gibt 





def test(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
x = test(11)
































print(f"x hat den Typ: {type(x)} und den Wert: {x}")