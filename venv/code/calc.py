# manages all calculator functions
import tkinter as tk
from tkinter import font as tkfont


class Calculator():
    def __init__(self, root) -> None:
        self._num_rows = 10
        self._num_cols = 10
        self._output_string = tk.StringVar()
        self._output_string.set("")
        self._result_string = tk.StringVar()
        self._result_string.set("0")
        self._raw_result = ""
        self._raw_buffer = ""
        self._output_buffer = self._create_output_buffer(root)
        self._result = self._create_result(root)
        self._decimal_active = False


        self._create_buttons(root)

#   CREATION
    def _create_calc(self, root):
        pass

    def _create_buttons(self, root):
        self._create_numbers(root)
        self._create_operators(root)
        self._create_misc_functions(root)

    def _create_numbers(self, root):
        self._button7 = self._seven_button(root)
        self._button8 = self._eight_button(root)
        self._button9 = self._nine_button(root)
        self._button4 = self._four_button(root)
        self._button5 = self._five_button(root)
        self._button6 = self._six_button(root)
        self._button1 = self._one_button(root)
        self._button2 = self._two_button(root)
        self._button3 = self._three_button(root)
        self._button0 = self._zero_button(root)
        self._buttondec = self._decimal_button(root)

    def _create_operators(self, root):
        self._buttondiv = self._division_button(root)
        self._buttonmult = self._multiply_button(root)
        self._buttonminus = self._minus_button(root)
        self._buttonplus = self._plus_button(root)
        self._buttonequal = self._equal_button(root)

    def _create_misc_functions(self, root):
        pass

    def _create_output_buffer(self, root):
        return tk.Label(root, textvariable=self._output_string, font=tkfont.Font(name="Terminal", size=36)).grid(row=0, column=0, padx=5, pady=5, columnspan=self._num_cols, sticky=tk.NW)
        
    
    def _create_result(self, root):
        return tk.Label(root, textvariable=self._result_string, font=tkfont.Font(name="Terminal", size=50)).grid(row=1, column=0, padx=5, pady=5, columnspan=self._num_cols, rowspan=2, sticky=tk.E)
    
    #   NUMBERS
    def _seven_button(self, root):
        return tk.Button(root, text='7', command=lambda: self._calc_button_pressed(7), font=tkfont.Font(name="Terminal", size=30)).grid(row=5, column=0, padx=2, pady=2, sticky=tk.NSEW)

    def _eight_button(self, root):
        return tk.Button(root, text='8', command=lambda: self._calc_button_pressed(8), font=tkfont.Font(name="Terminal", size=30)).grid(row=5, column=1,padx=2, pady=2, sticky=tk.NSEW)
    
    def _nine_button(self, root):
        return tk.Button(root, text='9', command=lambda: self._calc_button_pressed(9), font=tkfont.Font(name="Terminal", size=30)).grid(row=5, column=2, padx=2, pady=2, sticky=tk.NSEW)
    
    def _four_button(self, root):
        return tk.Button(root, text='4', command=lambda: self._calc_button_pressed(4), font=tkfont.Font(name="Terminal", size=30)).grid(row=6, column=0, padx=2, pady=2, sticky=tk.NSEW)
    
    def _five_button(self, root):
        return tk.Button(root, text='5', command=lambda: self._calc_button_pressed(5), font=tkfont.Font(name="Terminal", size=30)).grid(row=6, column=1, padx=2, pady=2, sticky=tk.NSEW)
    
    def _six_button(self, root):
        return tk.Button(root, text='6', command=lambda: self._calc_button_pressed(6), font=tkfont.Font(name="Terminal", size=30)).grid(row=6, column=2, padx=2, pady=2, sticky=tk.NSEW)

    def _one_button(self, root):
        return tk.Button(root, text='1', command=lambda: self._calc_button_pressed(1), font=tkfont.Font(name="Terminal", size=30)).grid(row=7, column=0, padx=2, pady=2, sticky=tk.NSEW)
    
    def _two_button(self, root):
        return tk.Button(root, text='2', command=lambda: self._calc_button_pressed(2), font=tkfont.Font(name="Terminal", size=30)).grid(row=7, column=1, padx=2, pady=2, sticky=tk.NSEW)
    
    def _three_button(self, root):
        return tk.Button(root, text='3', command=lambda: self._calc_button_pressed(3), font=tkfont.Font(name="Terminal", size=30)).grid(row=7, column=2, padx=2, pady=2, sticky=tk.NSEW)
    
    def _zero_button(self, root):
       return tk.Button(root, text='0', command=lambda: self._calc_button_pressed(0), font=tkfont.Font(name="Terminal", size=30)).grid(row=8, column=0, padx=2, pady=2, sticky=tk.NSEW)
    
    def _decimal_button(self, root):
        return tk.Button(root, text='.', command=lambda: self._calc_button_pressed("."), font=tkfont.Font(name="Terminal", size=30)).grid(row=8, column=1, padx=2, pady=2, sticky=tk.NSEW)

#   OPERATORS
    def _division_button(self, root):
        return tk.Button(root, text="/", command=lambda: self._calc_button_pressed("/"), font=tkfont.Font(name="Terminal", size=30)).grid(row=5, column=3, padx=2, pady=2, sticky=tk.NSEW)

    def _multiply_button(self, root):
        return tk.Button(root, text="*", command=lambda: self._calc_button_pressed("*"), font=tkfont.Font(name="Terminal", size=30)).grid(row=6, column=3, padx=2, pady=2, sticky=tk.NSEW)

    def _minus_button(self, root):
        return tk.Button(root, text="-", command=lambda: self._calc_button_pressed("-"), font=tkfont.Font(name="Terminal", size=30)).grid(row=7, column=3, padx=2, pady=2, sticky=tk.NSEW)

    def _plus_button(self, root):
        return tk.Button(root, text="+", command=lambda: self._calc_button_pressed("+"), font=tkfont.Font(name="Terminal", size=30)).grid(row=8, column=3, padx=2, pady=2, sticky=tk.NSEW)

    def _equal_button(self, root):
        return tk.Button(root, text="=", command=lambda: self._calc_button_pressed("="), font=tkfont.Font(name="Terminal", size=30)).grid(row=8, column=2, padx=2, pady=2, sticky=tk.NSEW)

#   CALCULATION
    def _calc_button_pressed(self, button_val):
        if isinstance(button_val, int):
            self._raw_buffer = f"{self._raw_buffer}{button_val}"
            self._output_string.set(self._raw_buffer)
            return
        elif button_val == ".":
            if not self._decimal_active:
                self._decimal_active = True
                self._raw_buffer = f"{self._raw_buffer}{button_val}"
                self._output_string.set(self._raw_buffer)
            return
        elif button_val == "/" or "*" or "-" or "+":
            self._decimal_active = False
            self._raw_buffer = f"{self._raw_buffer} {button_val} "
            self._output_string.set(self._raw_buffer)
            return
        elif button_val == "backspace":
            pass
        elif button_val == "clear":
            pass
        elif button_val == "=":
            pass
        
        
        
        












#   CALCULATING FROM STRING
#equation_string = "2 * (4 - 3) + 10"
#result = eval(equation_string)
#print(result)  # Output: 12