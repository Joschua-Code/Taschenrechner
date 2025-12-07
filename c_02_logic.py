
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
            self.gui.number1_label.configure(textvariable="", text=f"{self.gui.number1.get():,.0f}")
        else:       
            self.gui.number1_label.configure(textvariable="", text=f"{self.gui.number1.get():,.{self.gui.number1_comma_position-1}f}")

    def set_operator(self):
        if self.gui.operator_null.get():
            self.gui.operator_label.configure(textvariable=self.gui.operator)
        else:
            self.gui.operator_label.configure(textvariable=self.gui.operator)
    
    def set_number_2(self): #Only to be called by enter_number()
        if self.gui.number2_null.get() == True:
            return
        
        if self.gui.number2_comma_position == 0:
            self.gui.number2_label.configure(textvariable="", text=f"{self.gui.number2.get():,.0f}")
        else:       
            self.gui.number2_label.configure(textvariable="", text=f"{self.gui.number2.get():,.{self.gui.number2_comma_position-1}f}")
    
    def set_equal(self):
        if self.gui.equal_null.get():
            self.gui.equal_label.configure(textvariable=self.gui.equal)
        else:
            self.gui.equal_label.configure(textvariable=self.gui.equal)

    def set_result(self):
        if self.gui.result_null.get():
            self.gui.result_label.configure(textvariable="")
        elif self.gui.result.get() % 1 == 0:
            self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():,.0f}")
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
                self.gui.result.set(self.gui.number1.get() + self.gui.number2.get())
                self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():,}")
                print(f"{self.gui.result.get():,}")
                print("here !")

            elif self.gui.operator.get() == "-":
                self.gui.result.set(self.gui.number1.get() - self.gui.number2.get())
                self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():,}")

            elif self.gui.operator.get() == "x":
                self.gui.result.set(self.gui.number1.get() * self.gui.number2.get())
                self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():,}")

            elif self.gui.operator.get() == "/":
                self.gui.result.set(self.gui.number1.get() / self.gui.number2.get())
                self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():,}")
                
            #if self.gui.number1_comma_position >= self.gui.number2_comma_position:
            #    self.gui.result_label.configure(textvariable="", text=f"{self.gui.result.get():.{self.gui.number1_comma_position-1}f}")
            #else:




            self.gui.result_null.set(False)
            self.gui.equal_null.set(False)
            self.gui.equal.set("=")
            self.check()
                      

    #Clears the Result window except it keeps the result value and puts it in the Number 1 Frame
    def next_calculation(self):
        n1 = self.gui.number1.get()
        n2 = self.gui.number2.get()
        r = self.gui.result.get()
        self.clear()
        self.enter_number(r)
        self.gui.entry_at_field_one.set(False)

    def clear(self):
        self.gui.number1_null.set(True)
        self.gui.number1.set("")
        self.gui.number1_label.configure(text="")
        self.gui.operator_null.set(True)
        self.gui.operator.set("")
        self.gui.number2_null.set(True)
        self.gui.number2.set("")
        self.gui.number2_label.configure(text="")
        self.gui.equal_null.set(True)
        self.gui.equal.set("")
        self.gui.result_null.set(True)
        self.gui.result.set("")
        self.gui.result_label.configure(text="")
        self.gui.entry_at_field_one.set(True)
        self.gui.number1_comma_position = 0
        self.gui.number2_comma_position = 0
        self.check()


    def set_operator_window(self, x):
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

            if x == "/":
                self.next_calculation()
                self.gui.operator.set("/")
            elif x == "x":
                self.next_calculation()
                self.gui.operator.set("x")
            elif x == "-":
                self.next_calculation()
                self.gui.operator.set("-")
            elif x == "+":
                self.next_calculation()
                self.gui.operator.set("+")
        self.check()
        

    def change_plus_minus(self):
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
            self.gui.number1_comma_position += 1
        else:
            self.gui.number2_comma_position += 1


    def enter_number(self, x):
        if self.gui.entry_at_field_one.get():                               # --- For Number 1 ---

            if self.gui.number1_null.get(): #No number assigned so far
                self.gui.number1_null.set(False)
                self.gui.number1.set(x)
            else:
                if self.gui.number1_comma_position == 0:    #Not a decimal Number
                    self.gui.number1.set(self.gui.number1.get() * 10 + x)
                else:                                       #The new number shall be fractional
                    self.gui.number1.set(self.gui.number1.get() + x * (0.1 ** self.gui.number1_comma_position)) 
                    self.gui.number1_comma_position += 1

        else:                                                               # --- For Number 2 ---
            if self.gui.number2_null.get(): #No number assigned so far
                self.gui.number2_null.set(False)
                self.gui.number2.set(x)

            else:
                if self.gui.number2_comma_position == 0: #Not a decimal Number
                    self.gui.number2.set(self.gui.number2.get() * 10 + x)
                else:                                    #The new number shall be fractional
                    self.gui.number2.set(self.gui.number2.get() + x * (0.1 ** self.gui.number2_comma_position))
                    self.gui.number2_comma_position += 1

        print(self.gui.number1.get())
        self.check()
        print(self.gui.number1.get())

