import tkinter as tk
from tkinter import ttk
import sys


#Goals and maybe goals
#Giving every button his function
    #Implementing the history button
        #Making a list function that saves every result
#Implementing the Keyboard to insert Numbers or Operators
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

number1_null = tk.BooleanVar()
number1_null.set(True)
number1 = tk.IntVar()
number1.set(0)

number1_label = ttk.Label(ergebnisfenster) 
number1_label.grid(row=0, column=0)

def set_number_1():
    if number1_null.get():
        number1_label.configure(textvariable="")
    else:
        number1_label.configure(textvariable=number1)
set_number_1()

operator_null = tk.BooleanVar()
operator_null.set(True)
operator = tk.StringVar()
operator.set("+")

operator_label = ttk.Label(ergebnisfenster)
operator_label.grid(row=0, column=1)

def set_operator():
    if operator_null.get():
        operator_label.configure(textvariable="")
    else:
        operator_label.configure(textvariable=operator)
set_operator()


number2_null = tk.BooleanVar()
number2_null.set(True)
number2 = tk.IntVar()
number2.set(0)

number2_label = ttk.Label(ergebnisfenster)
number2_label.grid(row=0, column=2)

def set_number_2():
    if number2_null.get():
        number2_label.configure(textvariable="")
    else:
        number2_label.configure(textvariable=number2)
set_number_2()



equal_null = tk.BooleanVar()
equal_null.set(True)
equal = tk.StringVar()
equal.set("=")

equal_label = ttk.Label(ergebnisfenster)
equal_label.grid(row=0, column=3)

def set_equal():
    if equal_null.get():
        equal_label.configure(textvariable="")
    else:
        equal_label.configure(textvariable=equal)
set_equal()


result_null = tk.BooleanVar()
result_null.set(True)
result = tk.IntVar()
result.set(0)

result_label = ttk.Label(ergebnisfenster)
result_label.grid(row=0, column=4)

def set_result():
    if result_null.get():
        result_label.configure(textvariable="")
    else:
        result_label.configure(textvariable=result)
set_result()


distance_holder_label = ttk.Label(window)
distance_holder_label.grid(row=1, column=0)
distance_holder_label.configure(textvariable="")



pointer_number = 0

def calculate():
    if operator.get() != "" and number2.get() != "":
        print("hi")
        #result_label.configure(textvariable=number1) = number1

calculate()

def check():
    set_number_1()
    set_operator()
    set_number_2()
    set_equal()
    set_result()

set_next_number_behind_comma = tk.BooleanVar(value = False)

entry_at_field_one = tk.BooleanVar(value = True)


def enter_number(x):
    if entry_at_field_one.get():
    
        if number1_null.get():
            number1_null.set(False)
            number1.set(x)

        elif number1.get() % 1 != 0 or set_next_number_behind_comma.get():
            number1.set(number1.get() + x / 100)
            print(number1.get())
            set_next_number_behind_comma.set(False)

        else:
            number1.set(number1.get() * 10 + x)
    else:
        if number2_null.get():
            number2_null.set(False)
            number2.set(x)

        elif number2.get() % 1 != 0 or set_next_number_behind_comma.get():
            number2.set(number2.get() + x / 100)
            print(number2.get())
            set_next_number_behind_comma.set(False)

        else:
            number2.set(number2.get() * 10 + x)


        
    check()





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

########################################################################## Current Place of Implementation
def set_operator_divide():
    operator_null.set(False)
    entry_at_field_one.set(False)
    operator.set("/")
    check()

def set_operator_window(x):
    operator_null.set(False)
    entry_at_field_one.set(False)

    if x == "/":
        operator.set("/")
    elif x == "x":
        operator.set("x")
    elif x == "-":
        operator.set("-")
    elif x == "+":
        operator.set("+")
    
    check()
    


divide_button = ttk.Button(
    window, 
    text="/", 
    command=lambda: set_operator_window("/")
    )
divide_button.grid(row=3, column=3)


seven_button = ttk.Button(
    window, 
    text=7, 
    command=lambda: enter_number(7)
    )
seven_button.grid(row=4, column=0)


eight_button = ttk.Button(
    window, 
    text=8, 
    command=lambda: enter_number(8)
    )
eight_button.grid(row=4, column=1)


nine_button = ttk.Button(
    window,
    text=9,
    command=lambda: enter_number(9)
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
    command=lambda: enter_number(4)
)
four_button.grid(row=5, column=0)


five_button = ttk.Button(
    window,
    text=5,
    command=lambda: enter_number(5)
)
five_button.grid(row=5, column=1)


six_button = ttk.Button(
    window,
    text=6,
    command=lambda: enter_number(6)
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
    command=lambda: enter_number(1)
)
one_button.grid(row=6, column=0)


two_button = ttk.Button(
    window,
    text=2,
    command=lambda: enter_number(2)
)
two_button.grid(row=6, column=1)


three_button = ttk.Button(
    window,
    text=3,
    command=lambda: enter_number(3)
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
    command=lambda: enter_number(0)
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





















#print("Für Addition tippe 'plus' für Subtraktion 'minus' für Multiplikation 'mal' und für Division 'geteilt'")
#rechnug = str(input())
#
#if rechnug == "plus":
#    plus_ergebnis = plus(x,y)
#    print("Das Ergebnis ist:", plus_ergebnis)
#
#elif rechnug == "minus":
#    minus_ergebnis = minus(x,y)
#    print("Das Ergebnis ist:", minus_ergebnis)
#
#elif rechnug == "mal":
#    mal_ergebnis = mal(x,y)
#    print("Das Ergebnis ist:", mal_ergebnis)
#
#elif rechnug == "geteilt":
#    geteilt_ergebnis = geteilt(x,y)
#    print("Das Ergebnis ist:", geteilt_ergebnis)