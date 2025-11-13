import tkinter as tk
from tkinter import ttk
import sys

window = tk.Tk()
window.title("Taschenrechner")
window.geometry("400x550")
window.minsize(width=250,height=300)
window.configure(padx= 50, pady=50)
#window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="cols")

ergebnisfenster = tk.Frame(window)
ergebnisfenster.grid(row=0, column=0, columnspan=4, sticky="ew")
ergebnisfenster.grid_columnconfigure((0,1,2,3,4), weight=1, uniform="cols")

#Taschenrechner

#Ergebnisfenster (Zahl1 - Operator - Zahl2 - Ergebnis)
#Erste Zahl
zahl1 = tk.IntVar()
zahl1.set(1)

zahl1_label = ttk.Label(ergebnisfenster)
zahl1_label.grid(row=0, column=0)
zahl1_label.configure(textvariable=zahl1)


#Operator
operator = tk.StringVar()
operator.set("+")

operator_label = ttk.Label(ergebnisfenster)
operator_label.grid(row=0, column=1)
operator_label.configure(textvariable=operator)


#Zweite Zahl
zahl2 = tk.IntVar()
zahl2.set(2)

zahl2_label = ttk.Label(ergebnisfenster)
zahl2_label.grid(row=0, column=2)
zahl2_label.configure(textvariable=zahl2)


#Gleichzeichenlabel
gleichzeichen_label = ttk.Label(ergebnisfenster)
gleichzeichen_label.grid(row=0, column=3)

gleichzeichen = tk.StringVar()
gleichzeichen.set("=")
gleichzeichen_label.configure(textvariable=gleichzeichen)

#Ergebnislabel
ergebnis = tk.IntVar()
ergebnis.set(3)

ergebnis_label = ttk.Label(ergebnisfenster)
ergebnis_label.grid(row=0, column=4)
ergebnis_label.configure(textvariable=ergebnis)


#Abstandshalter
ergebnis_label = ttk.Label(window)
ergebnis_label.grid(row=1, column=0)
ergebnis_label.configure(textvariable="")




#ClearButton
clear = ttk.Button(
    window, 
    text="C", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
clear.grid(row=3, column=0)

#back_button
back = ttk.Button(
    window, 
    text="⌫", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
back.grid(row=3, column=1)


#History button
history = ttk.Button(
    window, 
    text="☰", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
history.grid(row=3, column=2)


#Divide button
help = ttk.Button(
    window, 
    text="?", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
help.grid(row=3, column=3)

















"""
label1 = ttk.Label(window)
label1.pack()
text1 = tk.StringVar()
text1.set("Hallo")
label1.configure(textvariable=text1)

label2 = ttk.Label(window)
label2.pack()
text2 = tk.StringVar()
text2.set("Hallo2")
label2.configure(textvariable=text2)


text2.set(text2.get() + " " + text2.get())


lzahl1_int = tk.IntVar()
lzahl1_int.set(1000)

lzahl1 = ttk.Label(window, textvariable=lzahl1_int)
lzahl1.pack()
lzahl1.configure(relief="solid")


button1 = ttk.Button(
    window, 
    text="Hallo", 
    command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
button1.pack()
"""






window.mainloop()
print("Du hast den Taschenrechner geschlossen")

#Beendet das Programm an diesem Punkt
sys.exit(0)


























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