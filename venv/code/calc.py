# manages all calculator functions
import tkinter as tk


class Calculator():
    pass

class CalcButton(tk.Button):
    def __init__(self, root, text, width, height, row, column, rowspan=1, columnspan=1):
        super().__init__(master=root, text=text, width=width, height=height)
        self.grid(column=column, row=row, rowspan=rowspan, columnspan=columnspan)