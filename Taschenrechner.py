import tkinter as tk
from tkinter import ttk
import sys


#Goals and maybe goals
#Giving every button his function
    #Implementing the history button
        #Making a list function that saves every result
#Making the buttons having more height
#Buttons adjusting to and filling the window
#Style
    #Making the background fancier if possible - slightly grey and blueish? - see throu would be optimal
    #Making the buttons fancy - brighter colour than background
    #If possible making the frame of the program dark and transparent and the name of the program in the center


#Window and Frames
window = tk.Tk()
window.title("Taschenrechner")
window.geometry("400x225")
window.minsize(width=250,height=300)
window.configure(padx= 50, pady=50)
#window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="cols")

ergebnisfenster = tk.Frame(window)
ergebnisfenster.grid(row=0, column=0, columnspan=4, sticky="ew")
ergebnisfenster.grid_columnconfigure((0,1,2,3,4), weight=1, uniform="cols")



#Resultwindow (Number 1 - Operator - Number 2 - Result)


number1 = tk.IntVar()
number1.set(1)

number1_label = ttk.Label(ergebnisfenster)
number1_label.grid(row=0, column=0)
number1_label.configure(textvariable=number1)


operator = tk.StringVar()
operator.set("+")

operator_label = ttk.Label(ergebnisfenster)
operator_label.grid(row=0, column=1)
operator_label.configure(textvariable=operator)


number2 = tk.IntVar()
number2.set(2)

number2_label = ttk.Label(ergebnisfenster)
number2_label.grid(row=0, column=2)
number2_label.configure(textvariable=number2)


equal_label = ttk.Label(ergebnisfenster)
equal_label.grid(row=0, column=3)

equal = tk.StringVar()
equal.set("=")
equal_label.configure(textvariable=equal)


result = tk.IntVar()
result.set(3)

result_label = ttk.Label(ergebnisfenster)
result_label.grid(row=0, column=4)
result_label.configure(textvariable=result)


distance_holder_label = ttk.Label(window)
distance_holder_label.grid(row=1, column=0)
distance_holder_label.configure(textvariable="")


#It follows: Clear / Backspace / History / Operator and Number Buttons

clear_button = ttk.Button(
    window, 
    text="C", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
clear_button.grid(row=3, column=0)


back_button = ttk.Button(
    window, 
    text="⌫", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
back_button.grid(row=3, column=1)


history_button = ttk.Button(
    window, 
    text="☰", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
history_button.grid(row=3, column=2)


divide_button = ttk.Button(
    window, 
    text="/", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
divide_button.grid(row=3, column=3)


seven_button = ttk.Button(
    window, 
    text=7, 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
seven_button.grid(row=4, column=0)


eight_button = ttk.Button(
    window, 
    text=8, 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
eight_button.grid(row=4, column=1)


nine_button = ttk.Button(
    window,
    text=9,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
nine_button.grid(row=4, column=2)


multiplication_button = ttk.Button(
    window, 
    text="x", 
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
    )
multiplication_button.grid(row=4, column=3)


four_button = ttk.Button(
    window,
    text=4,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
four_button.grid(row=5, column=0)


five_button = ttk.Button(
    window,
    text=5,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
five_button.grid(row=5, column=1)


six_button = ttk.Button(
    window,
    text=6,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
six_button.grid(row=5, column=2)


minus_button = ttk.Button(
    window,
    text="-",
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
minus_button.grid(row=5, column=3)


one_button = ttk.Button(
    window,
    text=1,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
one_button.grid(row=6, column=0)


two_button = ttk.Button(
    window,
    text=2,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
two_button.grid(row=6, column=1)


three_button = ttk.Button(
    window,
    text=3,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
three_button.grid(row=6, column=2)

plus_button = ttk.Button(
    window,
    text="+",
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
plus_button.grid(row=6, column=3)

change_plus_minus_sign_button = ttk.Button(
    window,
    text="+/-",
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
change_plus_minus_sign_button.grid(row=7, column=0)


zero_button = ttk.Button(
    window,
    text=0,
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
zero_button.grid(row=7, column=1)

comma_button = ttk.Button(
    window,
    text=",",
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
comma_button.grid(row=7, column=2)

equal_button = ttk.Button(
    window,
    text="=",
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
equal_button.grid(row=7, column=3)






window.mainloop()
print("Du hast den Taschenrechner geschlossen.")

#Closes the program at this point.
sys.exit(0)



















"""

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

"""