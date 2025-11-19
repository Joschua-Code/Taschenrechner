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
#If changeing the operator after already having calculated - removing the result and equal sign
#When pressing equal again making the result the new number 1 and removing the rest
# Making the numbers slightly brighter than the other buttons and the equal button light blue or something
# Solving the problem of divididing by zero


#Known Bugs
#Comma doesnt work anymore
#Results doesnt have any fractional values anymore


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
number1.set("")


number1_label = ttk.Label(ergebnisfenster) 
number1_label.grid(row=0, column=0)

def set_number_1():
    if number1_null.get():
        number1_label.configure(textvariable=number1)
        print("Das hier sollte geprintet werden!")
    else:
        number1_label.configure(textvariable=number1)
        print("Das hier sollte nicht geprintet werden!")
set_number_1()

operator_null = tk.BooleanVar()
operator_null.set(True)
operator = tk.StringVar()
operator.set("")

operator_label = ttk.Label(ergebnisfenster)
operator_label.grid(row=0, column=1)

def set_operator():
    if operator_null.get():
        operator_label.configure(textvariable=operator)
    else:
        operator_label.configure(textvariable=operator)
set_operator()


number2_null = tk.BooleanVar()
number2_null.set(True)
number2 = tk.IntVar()
number2.set("")

number2_label = ttk.Label(ergebnisfenster)
number2_label.grid(row=0, column=2)

def set_number_2():
    if number2_null.get():
        number2_label.configure(textvariable=number2)
    else:
        number2_label.configure(textvariable=number2)
set_number_2()



equal_null = tk.BooleanVar()
equal_null.set(True)
equal = tk.StringVar()
equal.set("")

equal_label = ttk.Label(ergebnisfenster)
equal_label.grid(row=0, column=3)

def set_equal():
    if equal_null.get():
        equal_label.configure(textvariable=equal)
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



def check():
    set_number_1()
    set_operator()
    set_number_2()
    set_equal()
    set_result()

set_next_number_behind_comma = tk.BooleanVar(value = False)

entry_at_field_one = tk.BooleanVar(value = True)


def calculate():
    if operator.get() != "" and number2.get() != "":
        if operator.get() == "+":
            result.set(number1.get() + number2.get())

        elif operator.get() == "-":
            result.set(number1.get() - number2.get())

        elif operator.get() == "x":
            result.set(number1.get() * number2.get())

        elif operator.get() == "/":
            result.set(number1.get() / number2.get())
            
        if result.get() % 1 == 0:
            result.set(int(result.get()))

        result_null.set(False)
        equal_null.set(False)
        equal.set("=")
        check()


def next_calculation():
    n1 = number1.get()
    n2 = number2.get()
    r = result.get()
    clear()
    number1.set(r)
    entry_at_field_one.set(False)



def clear():
    number1_null.set(True)
    number1.set("")
    operator_null.set(True)
    operator.set("")
    number2_null.set(True)
    number2.set("")
    equal_null.set(True)
    equal.set("")
    result_null.set(True)
    result.set("")
    set_next_number_behind_comma.set(False)
    entry_at_field_one.set(True)
    check()



clear_button = ttk.Button(
    window, 
    text="C", 
    command=lambda: clear()
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


def set_operator_window(x):
    operator_null.set(False)
    entry_at_field_one.set(False)

    if result_null.get():

        if x == "/":
            operator.set("/")
        elif x == "x":
            operator.set("x")
        elif x == "-":
            operator.set("-")
        elif x == "+":
            operator.set("+")
    else:

        if x == "/":
            next_calculation()
            operator.set("/")
        elif x == "x":
            next_calculation()
            operator.set("x")
        elif x == "-":
            next_calculation()
            operator.set("-")
        elif x == "+":
            next_calculation()
            operator.set("+")
    
    check()
    


divide_button = ttk.Button(
    window, 
    text="/", 
    command=lambda: set_operator_window("/")
    )
divide_button.grid(row=3, column=3)


multiplication_button = ttk.Button(
    window, 
    text="x", 
    command=lambda: set_operator_window("x")
    )
multiplication_button.grid(row=4, column=3)



minus_button = ttk.Button(
    window,
    text="-",
    command=lambda: set_operator_window("-")
)
minus_button.grid(row=5, column=3)



plus_button = ttk.Button(
    window,
    text="+",
    command=lambda: set_operator_window("+")
)
plus_button.grid(row=6, column=3)

def change_plus_minus():
    if entry_at_field_one.get():
        if number1.get() == 0:
            return
        elif number1.get() >= 0:
            number1.set(number1.get() - 2 * number1.get())
        
change_plus_minus_sign_button = ttk.Button(
    window,
    text="+/-",
    command=lambda: change_plus_minus()
)
change_plus_minus_sign_button.grid(row=7, column=0)


comma_button = ttk.Button(
    window,
    text=",",
    #command=lambda: lzahl1_int.set(lzahl1_int.get()+1)
)
comma_button.grid(row=7, column=2)


equal_button = ttk.Button(
    window,
    text="=",
    command=lambda: calculate()
)
equal_button.grid(row=7, column=3)



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


numbers = {"Button_0" : {"num": 0, "row" : 7, "column" : 1},
           "Button_1" : {"num": 1, "row" : 6, "column" : 0},
           "Button_2" : {"num": 2, "row" : 6, "column" : 1},
           "Button_3" : {"num": 3, "row" : 6, "column" : 2},
           "Button_4" : {"num": 4, "row" : 5, "column" : 0},
           "Button_5" : {"num": 5, "row" : 5, "column" : 1},
           "Button_6" : {"num": 6, "row" : 5, "column" : 2},
           "Button_7" : {"num": 7, "row" : 4, "column" : 0},
           "Button_8" : {"num": 8, "row" : 4, "column" : 1},
           "Button_9" : {"num": 9, "row" : 4, "column" : 2}
        }

for name, value in numbers.items():
    item = ttk.Button(
        window,
        text = value["num"],
        command = lambda x = value["num"]: enter_number(x)
    )
    item.grid(row = value["row"], column = value["column"])









window.mainloop()
print("Du hast den Taschenrechner geschlossen.")

#Closes the program at this point.
sys.exit(0)