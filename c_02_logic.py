from decimal import Decimal
import tkinter as tk
from tkinter import ttk
from c_03_utils import as_decimal

class Logic():

    def __init__(self, gui_instance):
        self.gui = gui_instance #Here the reference to the instance of the class gui gets saved
        self.set_number_1()
        self.set_operator()
        self.set_number_2()
        self.set_equal()
        self.set_result()
        self.check()
    

    def set_history_instance(self, history_instance):
        self.history = history_instance


    def set_number_1(self): #Only to be called by enter_number()
        if self.gui.number1_null.get() == True:
            return
        
        if self.gui.number1_comma_position == 0:
            self.gui.number1.set(f"{Decimal(self.gui.number1.get()):,.0f}")
        else:       
            self.gui.number1.set(f"{Decimal(self.gui.number1.get()):,.{self.gui.number1_comma_position-1}f}")


    def set_operator(self):

        if self.gui.operator_null.get():
            self.gui.operator_label.configure(textvariable=self.gui.operator)

        else:
            self.gui.operator_label.configure(textvariable=self.gui.operator)
    

    def set_number_2(self): #Only to be called by enter_number()

        if self.gui.number2_null.get() == True:
            return
        
        if self.gui.number2_comma_position == 0:
            self.gui.number2.set(f"{Decimal(self.gui.number2.get()):,.0f}")

        else:       
            self.gui.number2.set(f"{Decimal(self.gui.number2.get()):,.{self.gui.number2_comma_position-1}f}")
    

    def set_equal(self):

        if self.gui.equal_null.get():
            self.gui.equal_label.configure(textvariable=self.gui.equal)

        else:
            self.gui.equal_label.configure(textvariable=self.gui.equal)


    def set_result(self):

        if self.gui.result_null.get():
            self.gui.result.set("")

        elif self.gui.result.get() % 1 == 0:
            self.gui.result.set(f"{Decimal(self.gui.result.get()):,.0f}")

        else:
            self.gui.result_label.configure(textvariable=self.gui.result)
            self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():,}")    
  

    def check(self):

        self.set_number_1()
        self.set_operator()
        self.set_number_2()
        self.set_equal()
        self.set_result()


    def calculate(self):

        if self.gui.operator.get() != "" and self.gui.number2.get() != "":

            if self.gui.operator.get() == "+":
                self.gui.result.set(f"{Decimal(self.gui.number1.get()) + Decimal(self.gui.number2.get())}")

            elif self.gui.operator.get() == "-":
                self.gui.result.set(f"{Decimal(self.gui.number1.get()) - Decimal(self.gui.number2.get())}")

            elif self.gui.operator.get() == "x":
                self.gui.result.set(f"{Decimal(self.gui.number1.get()) * Decimal(self.gui.number2.get())}")

            elif self.gui.operator.get() == "/":
                self.gui.result.set(f"{Decimal(self.gui.number1.get()) / Decimal(self.gui.number2.get())}")
    
            self.gui.equal.set("=")
            self.gui.equal_null.set(False)
            self.gui.result_null.set(False)
            self.check()


    #Clears the result window except it keeps the result value and puts it in the number 1 frame
    def next_calculation(self):

        n1 = self.gui.number1.get()
        n2 = self.gui.number2.get()
        r = self.gui.result.get()
        _, _, r_comma_position = self.getthelength(r)

        self.clear()
        self.gui.number1_comma_position = r_comma_position + 1
        self.enter_number(r)
        self.gui.entry_at_field_one.set(False)


    def clear(self):

        self.gui.number1_null.set(True)
        self.gui.number1.set("")
        self.gui.operator_null.set(True)
        self.gui.operator.set("")
        self.gui.number2_null.set(True)
        self.gui.number2.set("")
        self.gui.equal_null.set(True)
        self.gui.equal.set("")
        self.gui.result_null.set(True)
        self.gui.result.set("")
        self.gui.entry_at_field_one.set(True)
        self.gui.number1_comma_position = 0
        self.gui.number2_comma_position = 0
        self.check()


    def set_operator_window(self, x):

        if self.gui.number1.get() == "":
            return
        
        self.gui.operator_null.set(False)
        self.gui.entry_at_field_one.set(False)

        if self.gui.result_null.get():
            if x == "/":
                self.gui.operator.set("/")
            elif x == "x":
                self.gui.operator.set("x")
            elif x == "-":
                self.gui.operator.set("-")
            elif x == "+":
                self.gui.operator.set("+")

        else:
            self.next_calculation()
            if x == "/":
                self.gui.operator.set("/")
            elif x == "x":
                self.gui.operator.set("x")
            elif x == "-":
                self.gui.operator.set("-")
            elif x == "+":
                self.gui.operator.set("+")

        self.check()
        

    def change_plus_minus(self):
        if self.gui.result_null.get() != True: #Checks if Result is Null if not it blocks entering a Number after already calculating
            return
        
        if self.gui.entry_at_field_one.get():
            if self.gui.number1.get() == 0:
                return
            else:
                self.gui.number1.set(self.gui.number1.get() * -1)
                self.set_number_1()
        else:
            if self.gui.number2.get() == 0:
                return
            else:
                self.gui.number2.set(self.gui.number2.get() * -1)
                self.set_number_2()


    def comma_pressed(self):        
        if self.gui.entry_at_field_one.get():
            if self.gui.number1_comma_position == 0:
                self.gui.number1_comma_position += 1
        else:
            if self.gui.number2_comma_position == 0:
                self.gui.number2_comma_position += 1


    def enter_number(self, x):
        if self.gui.result.get() != "": #Checks if Result is Null if not it blocks entering a Number after already calculating
            return
        
        if self.gui.entry_at_field_one.get():                               # --- For Number 1 ---

            if self.gui.number1.get() == "": #No number assigned so far
                self.gui.number1.set(x)

            else:
                if self.gui.number1_comma_position == 0:    #Not a decimal Number
                    if as_decimal(self.gui.number1.get()) >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number1.set(as_decimal(self.gui.number1.get()) * 10 + x)

                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number1.set(as_decimal(self.gui.number1.get()) * 10 - x)

                else:                                       #The new number shall be fractional
                    if as_decimal(self.gui.number1.get()) >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number1.set(as_decimal(self.gui.number1.get()) + x * (as_decimal(0.1) ** self.gui.number1_comma_position)) 

                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number1.set(self.gui.number1.get() - x * (0.1 ** self.gui.number1_comma_position)) 

                    self.gui.number1_comma_position += 1

            if self.gui.number1_null.get() == False and self.is_length_under_9(self.gui.number1.get(), self.gui.number1_comma_position) == False: #Checking if entering exceeds the limit of 8 digits
                self.over_8_numbers("Number 1")
                return
            
        else:                                                               # --- For Number 2 ---
            if self.gui.number2_null.get(): #No number assigned so far
                self.gui.number2_null.set(False)
                self.gui.number2.set(x)

            else:
                if self.gui.number2_comma_position == 0: #Not a decimal Number
                    if self.gui.number2.get() >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number2.set(self.gui.number2.get() * 10 + x)
                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number2.set(self.gui.number2.get() * 10 - x)

                else:                                    #The new number shall be fractional
                    if self.gui.number2.get() >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number2.set(self.gui.number2.get() + x * (0.1 ** self.gui.number2_comma_position))
                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number2.set(self.gui.number2.get() - x * (0.1 ** self.gui.number2_comma_position))
                    self.gui.number2_comma_position += 1

        self.check()


    def test(self):
        popup = tk.Toplevel(self.gui.window)
        popup.transient(self.gui.window)
        popup.grab_set()
        popup.resizable(False, False)
        x_window = self.gui.window.winfo_x()
        y_window = self.gui.window.winfo_y()
        width_window = self.gui.window.winfo_width()
        height_window = self.gui.window.winfo_height()
        popup.iconbitmap("Icon_Calculator_16x16.ico")
        popup.title("Hinweis")
        #Size of popup
        w = 200
        h = 100

        #Calculating the middle point of window
        x_popup = x_window + (width_window - w) // 2
        y_popup = y_window + (height_window - h) // 2

        popup.geometry(f"{w}x{h}+{x_popup}+{y_popup}")


    def over_8_numbers(self, a):
        x = f"Limit for {a} reached"
        popup = tk.Toplevel(self.gui.window)
        popup.transient(self.gui.window)
        popup.grab_set()
        popup.resizable(False, False)
        x_window = self.gui.window.winfo_x()
        y_window = self.gui.window.winfo_y()
        width_window = self.gui.window.winfo_width()
        height_window = self.gui.window.winfo_height()
        popup.iconbitmap("Icon_Calculator_16x16.ico")
        popup.title(x)

        #Size of popup
        w = 390
        h = 150

        #Calculating the middle point of window
        x_popup = x_window + (width_window - w) // 2
        y_popup = y_window + (height_window - h) // 2

        popup.geometry(f"{w}x{h}+{x_popup}+{y_popup}")

        popup.columnconfigure(0, weight=1)
        popup.rowconfigure(0, weight=1)
        self.warning_label = ttk.Label(popup, anchor="center", justify="center") 
        self.warning_label.grid(row=0, column=0)
        self.warning = tk.StringVar()
        self.warning.set("To keep the design simple, the maximum number of digits is set to 8. \n It seems you wanted to go far and beyond. \n Dont. :)")
        self.warning_label.configure(textvariable=self.warning)
        self.warning_label.grid(row=0, column=0)
        self.clear()


    def getthelength(self, x, commaposition) -> tuple[int, int, int]:  

        if x % 1 == 0:
            x = int(x)
            total_length = full_numbers_length = len(str(x))
            return total_length, full_numbers_length, 0
        
        else:
            x = float(str(f"{x:{commaposition}.f}"))
            total_length = len(str(x)) - 1
            full_numbers_length, decimal_length = str(x).split(".")
            full_numbers_length, decimal_length = len(full_numbers_length), len(decimal_length)
            return total_length, full_numbers_length, decimal_length
        

    def is_length_under_9(self, x, commaposition) -> bool:

        total_length, _, _ = self.getthelength(x, commaposition)

        return total_length < 9


    
