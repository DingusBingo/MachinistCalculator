#!/usr/bin/env python 
import tkinter as tk
from calc import Calculator


class Application():
    def __init__(self) -> None:
        self._root = tk.Tk()
        self._calc_frame = tk.Frame(self._root)
        self._root.title('Machinist Calculator')
        self._grid = tk.Grid()
        self._num_calc_rows = 9
        self._num_calc_cols = 4
        self._calc = Calculator(self._calc_frame)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self._close)
        self._set_calc_cell_size()
        self._calc_frame.tkraise()
    
    def _redraw(self):
        self._calc_frame.update_idletasks()
        self._calc_frame.update()
    
    def _wait_for_close(self):
        self._running = True

        while self._running:
            self._redraw()

    def _close(self):
        self._running = False

    def _set_calc_cell_size(self):
        for i in range(self._num_calc_rows):
            self._calc_frame.grid_rowconfigure(index=i, minsize=100)
        for i in range(self._num_calc_cols):
            self._calc_frame.grid_columnconfigure(index=i, minsize=100)

app = Application()
app._wait_for_close()


















#class Application(tk.Frame):
#    def __init__(self, master=None):
#        tk.Frame.__init__(self, master)
#        self.grid()
#        self.createWidgets()
#    
#    def createWidgets(self):
#        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
#        self.quitButton.grid()  
#
#app = Application() 
#app.master.title('Sample application') 
#app.mainloop()        