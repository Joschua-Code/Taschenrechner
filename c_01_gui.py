import tkinter as tk
from tkinter import ttk
import sys
import c_02_logic
from decimal import Decimal
from c_03_utils import as_decimal

class GUI:
    def __init__(self):
        
        self.initialize_window_and_variables()

        self.logic = c_02_logic.Logic(self)

        self.window.mainloop()

    def initialize_window_and_variables(self):
        #Window & Windowsettings
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("400x200")
        self.window.minsize(width=250,height=300)
        self.window.configure(padx= 50, pady=50)
        self.window.resizable(False, False)
        self.window.iconbitmap("Icon_Calculator_16x16.ico")


        #Resultframe - (Number 1 - Operator - Number 2 - Result)

        #Resultframe
        self.ergebnisfenster = tk.Frame(self.window)
        self.ergebnisfenster.grid(row=0, column=0, columnspan=4, sticky="ew")
        self.ergebnisfenster.grid_columnconfigure((0,1,2,3,4), weight=1, uniform="cols")


        #Pointer to the current entryfield
        self.entry_at_field_one = tk.BooleanVar(value = True)

        #Resultframe - (Number 1) - Creation of Label
        self.number1_label = ttk.Label(self.ergebnisfenster) 
        self.number1_label.grid(row=0, column=0)

        #Resultframe - (Number 1) - Creation of Variable
        self.number1 = tk.StringVar()
        self.number1.set("")
        self.number1_label.configure(textvariable=self.number1)

        #Resultframe - (Number 1) - Boolean for checking if Variable is initialized
        self.number1_null = tk.BooleanVar()
        self.number1_null.set(True)

        #Commaposition of Number 1
        self.number1_comma_position = 0


        #Resultframe - (Operator) - Creation of Label
        self.operator_label = ttk.Label(self.ergebnisfenster)
        self.operator_label.grid(row=0, column=1)

        #Resultframe - (Operator) - Creation of Variable
        self.operator = tk.StringVar()
        self.operator.set("")

        #Resultframe - (Operator) - Boolean for checking if Variable is initialized
        self.operator_null = tk.BooleanVar()
        self.operator_null.set(True)

        #Commaposition of Number 2
        self.number2_comma_position = 0

        #Resultframe - (Number 2) - Creation of Label
        self.number2_label = ttk.Label(self.ergebnisfenster)
        self.number2_label.grid(row=0, column=2)

        #Resultframe - (Number 2) - Creation of Variable
        self.number2 = tk.StringVar()
        self.number2.set("")

        #Resultframe - (Number 2) - Boolean for checking if Variable is initialized
        self.number2_null = tk.BooleanVar()
        self.number2_null.set(True)


        #Resultframe - (Equal) - Creation of Label
        self.equal_label = ttk.Label(self.ergebnisfenster)
        self.equal_label.grid(row=0, column=3)
        
        #Resultframe - (Equal) - Creation of Variable
        self.equal = tk.StringVar()
        self.equal.set("")

        #Resultframe - (Equal) - Boolean for checking if Variable is initialized
        self.equal_null = tk.BooleanVar()
        self.equal_null.set(True)


        #Resultframe - (Result)
        self.result_null = tk.BooleanVar()
        self.result_null.set(True)

        self.result = tk.DoubleVar()
        self.result.set(0)

        self.result_label = ttk.Label(self.ergebnisfenster)
        self.result_label.grid(row=0, column=4)


        #Distanceholderframe
        self.distance_holder_label = ttk.Label(self.window)
        self.distance_holder_label.grid(row=1, column=0)
        self.distance_holder_label.configure(textvariable="")


        #Buttons

        self.clear_button = ttk.Button(
            self.window, 
            text="C", 
            command=lambda: self.logic.clear()
        )
        self.clear_button.grid(row=3, column=0)


        self.back_button = ttk.Button(
            self.window, 
            text="⌫", 
            #command=lambda: ---------------------------------------------- ᕦ(＾O＾)ᕥ WORK IN PROGRESS ᕦ(＾O＾)ᕥ ----------------------------------------------                                   
            )
        self.back_button.grid(row=3, column=1)


        self.history_button = ttk.Button(
            self.window, 
            text="☰Test☰", 
            command=lambda: self.logic.over_8_numbers()
            )
        self.history_button.grid(row=3, column=2)


        self.divide_button = ttk.Button(
            self.window, 
            text="/", 
            command=lambda: self.logic.set_operator_window("/")
            )
        self.divide_button.grid(row=3, column=3)


        self.multiplication_button = ttk.Button(
            self.window, 
            text="x", 
            command=lambda: self.logic.set_operator_window("x")
            )
        self.multiplication_button.grid(row=4, column=3)


        self.minus_button = ttk.Button(
            self.window,
            text="-",
            command=lambda: self.logic.set_operator_window("-")
        )
        self.minus_button.grid(row=5, column=3)

        
        self.plus_button = ttk.Button(
            self.window,
            text="+",
            command=lambda: self.logic.set_operator_window("+")
        )
        self.plus_button.grid(row=6, column=3)


        self.change_plus_minus_sign_button = ttk.Button(
            self.window,
            text="+/-",
            command=lambda: self.logic.change_plus_minus()
        )
        self.change_plus_minus_sign_button.grid(row=7, column=0)


        self.comma_button = ttk.Button(
            self.window,
            text=".",
            command=lambda: self.logic.comma_pressed()
        )
        self.comma_button.grid(row=7, column=2)


        self.equal_button = ttk.Button(
            self.window,
            text="=",
            command=lambda: self.logic.calculate()
        )
        self.equal_button.grid(row=7, column=3)

        #The buttons 0 to 9 get initialized.
        self.numbers = {"Button_0" : {"num": 0, "row" : 7, "column" : 1},
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
        for name, value in self.numbers.items():
            self.item = ttk.Button(
                self.window,
                text = value["num"],
                command = lambda x = value["num"]: self.logic.enter_number(as_decimal(x))
            )
            self.item.grid(row = value["row"], column = value["column"])