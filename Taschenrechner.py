import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Taschenrechner")
root.geometry("400x600")
root.minsize(width=250,height=300)

label1 = ttk.Label(root)
label1.pack()
text1 = tk.StringVar()
text1.set("Hallo")
label1.configure(textvariable=text1)

label2 = ttk.Label(root)
label2.pack()
text2 = tk.StringVar()
text2.set("Hallo2")
label2.configure(textvariable=text2)


text2.set(text2.get() + " " + text2.get())









lzahl1_int = tk.IntVar()
lzahl1_int.set(1)
lzahl1 = ttk.Label(root, textvariable=lzahl1_int)
lzahl1.pack()
lzahl1.configure(relief="solid")


button1 = ttk.Button(
    root, 
    text="Hallo", 
    command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
button1.pack()







root.mainloop()
print("Du hast den Taschenrechner geschlossen")



























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