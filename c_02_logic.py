from decimal import Decimal
import tkinter as tk
from tkinter import ttk
from c_03_utils import as_decimal



class Logic():


    def __init__(self, gui_instance):
        self.gui = gui_instance #Here the reference to the instance of the class gui gets saved
        self.history_list = list()


    def calculate(self):

        if self.gui.operator.get() != "" and self.gui.number2.get() != "":

            if self.gui.operator.get() == "+":
                result = f"{Decimal(self.gui.number1.get()) + Decimal(self.gui.number2.get())}"
                if self.calculate_result_check(result):
                    self.gui.result.set(str(result))
                else:
                    if self.my_round(result) == "Too Long":
                        self.over_8_numbers("Result")
                        return
                    else:
                        result = self.my_round(result)
                        self.gui.result.set(str(result))

            elif self.gui.operator.get() == "-":
                result = f"{Decimal(self.gui.number1.get()) - Decimal(self.gui.number2.get())}"
                if self.calculate_result_check(result):
                    self.gui.result.set(str(result))
                else:
                    if self.my_round(result) == "Too Long":
                        self.over_8_numbers("Result")
                        return
                    else:
                        result = self.my_round(result)
                        self.gui.result.set(str(result))

            elif self.gui.operator.get() == "x":
                result = f"{Decimal(self.gui.number1.get()) * Decimal(self.gui.number2.get())}"
                if self.calculate_result_check(result):
                    self.gui.result.set(str(result))
                else:
                    if self.my_round(result) == "Too Long":
                        self.over_8_numbers("Result")
                        return
                    else:
                        result = self.my_round(result)
                        self.gui.result.set(str(result))

            elif self.gui.operator.get() == "/":
                result = f"{Decimal(self.gui.number1.get()) / Decimal(self.gui.number2.get())}"
                if self.calculate_result_check(result):
                    self.gui.result.set(str(result))
                else:
                    if self.my_round(result) == "Too Long":
                        self.over_8_numbers("Result")
                        return
                    else:
                        result = self.my_round(result)
                        self.gui.result.set(str(result))
    
            self.gui.equal.set("=")


    def calculate_result_check(self, result):
        if self.is_length_under_9(result):
            return True
        else:
            return False

        
    #Clears the result window except it keeps the result value and puts it in the number 1 frame
    def next_calculation(self):
        r = Decimal(self.gui.result.get())
        _, _, r_comma_position = self.getthelength(r)

        self.clear()
        self.gui.number1_comma_position = r_comma_position + 1
        self.enter_number(r)
        self.gui.entry_at_field_one.set(False)


    def clear(self):
        self.history(self.gui.number1.get(), self.gui.operator.get(), self.gui.number2.get(), self.gui.result.get())
        self.gui.number1.set("")
        self.gui.operator.set("")
        self.gui.number2.set("")
        self.gui.equal.set("")
        self.gui.result.set("")
        self.gui.entry_at_field_one.set(True)
        self.gui.number1_comma_position = 0
        self.gui.number2_comma_position = 0


    def set_operator_window(self, x):
        if self.gui.number1.get() == "":
            return
        
        self.gui.entry_at_field_one.set(False)
        if self.gui.result.get() == "":
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


    def change_plus_minus(self):
        if self.gui.result.get() != "": #Checks if Result is Null/Empty if not it blocks entering a Number after already calculating
            return
        
        if self.gui.entry_at_field_one.get():
            if self.gui.number1.get() == "":
                return
            else:
                self.gui.number1.set(f"{Decimal(self.gui.number1.get()) * -1}")
        else:
            if self.gui.number2.get() == "":
                return
            else:
                self.gui.number2.set(f"{Decimal(self.gui.number2.get()) * -1}")


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
                self.gui.number1.set(str(x))

            else:
                if self.gui.number1_comma_position == 0:    #Not a decimal Number
                    if as_decimal(self.gui.number1.get()) >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number1.set(str(as_decimal(self.gui.number1.get()) * 10 + x))

                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number1.set(str(as_decimal(self.gui.number1.get()) * 10 - x))

                else:                                       #The new number shall be fractional
                    if as_decimal(self.gui.number1.get()) >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number1.set(str(as_decimal(self.gui.number1.get()) + x * (as_decimal(0.1) ** self.gui.number1_comma_position))) 

                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number1.set(str(as_decimal(self.gui.number1.get()) - x * (as_decimal(0.1) ** self.gui.number1_comma_position))) 

                    self.gui.number1_comma_position += 1

            if self.gui.number1.get() != "" and self.is_length_under_9(self.gui.number1.get()) == False: #Checking if entering exceeds the limit of 8 digits
                self.over_8_numbers("Number 1")
                return
            
        else:                                                               # --- For Number 2 ---

            if self.gui.number2.get() == "": #No number assigned so far
                print(f"[enter_number] The Value for x that is to be inserted into Number2 is: {x}")
                self.gui.number2.set(str(x))

            else:
                if self.gui.number2_comma_position == 0: #Not a decimal Number
                    if as_decimal(self.gui.number2.get()) >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number2.set(str(as_decimal(self.gui.number2.get()) * 10 + x))

                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number2.set(str(as_decimal(self.gui.number2.get()) * 10 - x))

                else:                                    #The new number shall be fractional
                    if as_decimal(self.gui.number2.get()) >= 0: #Checks if the Number is positive or negative and then adds or substracts accordingly - 1v2
                        self.gui.number2.set(str(as_decimal(self.gui.number2.get()) + x * (as_decimal(0.1) ** self.gui.number2_comma_position)))

                    else: #Checks if the Number is positive or negative and then adds or substracts accordingly - 2v2
                        self.gui.number2.set(str(as_decimal(self.gui.number2.get()) - x * (as_decimal(0.1) ** self.gui.number2_comma_position)))

                    self.gui.number2_comma_position += 1

            if self.gui.number2.get() != "" and self.is_length_under_9(self.gui.number2.get()) == False: #Checking if entering exceeds the limit of 8 digits
                self.over_8_numbers("Number 2")
                return


   #def test(self):
   #    popup = tk.Toplevel(self.gui.window)
   #    popup.transient(self.gui.window)
   #    popup.grab_set()
   #    popup.resizable(False, False)
   #    x_window = self.gui.window.winfo_x()
   #    y_window = self.gui.window.winfo_y()
   #    width_window = self.gui.window.winfo_width()
   #    height_window = self.gui.window.winfo_height()
   #    popup.iconbitmap("Icon_Calculator_16x16.ico")
   #    popup.title("Hinweis")
   #    #Size of popup
   #    w = 200
   #    h = 100

   #    #Calculating the middle point of window
   #    x_popup = x_window + (width_window - w) // 2
   #    y_popup = y_window + (height_window - h) // 2

   #    popup.geometry(f"{w}x{h}+{x_popup}+{y_popup}")


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


    def getthelength(self, x) -> tuple[int, int, int]:  

        x = str(x)
        x = x.removeprefix("-")
        full_numbers, _, fractional = x.partition(".")
        full_numbers_length = len(full_numbers)
        fractional_numbers_length = len(fractional)        
        total_length = full_numbers_length + fractional_numbers_length

        return total_length, full_numbers_length, fractional_numbers_length
        
      
    def is_length_under_9(self, x) -> bool:

        total_length, _, _ = self.getthelength(x)

        return total_length <= 8


    def my_round(self, result):

        _, full_numbers_length, _ = self.getthelength(result)
        if full_numbers_length > 6:
            return "Too Long"

        to_reduce_number = 8 - full_numbers_length

        return (str(round(Decimal(result), to_reduce_number)))
    
    def backspace(self):
        if self.gui.result.get() != "":
            return
        
        if self.gui.entry_at_field_one.get(): #Field 1
            self.gui.number1.set(str(self.gui.number1.get())[:-1])

        if not self.gui.entry_at_field_one.get(): #Field 2
            self.gui.number2.set(str(self.gui.number2.get())[:-1])

    def history(self, n1, op, n2, r):
        if r == "":
            return
        self.history_list.append([n1, op, n2, "=", r])
        print(self.history_list)



    def history_gui(self):
        x = f"History"
        history_popup = tk.Toplevel(self.gui.window)
        history_popup.transient(self.gui.window)
        history_popup.grab_set()
        history_popup.resizable(False, False)
        x_window = self.gui.window.winfo_x()
        y_window = self.gui.window.winfo_y()
        width_window = self.gui.window.winfo_width()
        height_window = self.gui.window.winfo_height()
        history_popup.iconbitmap("Icon_Calculator_16x16.ico")
        history_popup.title(x)

        #Size of popup
        w = 390
        h = 190

        #Calculating the middle point of window
        x_history_popup = x_window + (width_window - w) // 2
        y_history_popup = y_window + (height_window - h) // 2

        history_popup.geometry(f"{w}x{h}+{x_history_popup}+{y_history_popup}")

        #history_popup.columnconfigure(0, weight=1)
        #history_popup.rowconfigure(0, weight=1)
        
        for row, calculation in enumerate(self.history_list):
            ttk.Label(history_popup, text=calculation).grid(row=row,column=0)

        self.warning_label = ttk.Label(history_popup, anchor="center", justify="center") 
        self.warning_label.grid(row=0, column=0)
        self.warning = tk.StringVar()
        self.warning.set("")
        self.warning_label.configure(textvariable=self.warning)
        self.warning_label.grid(row=0, column=0)






