#!/usr/bin/env python 
import tkinter as tk
from calc import Calculator


class Application():
    def __init__(self) -> None:
        self._root = tk.Tk()
        self._root.title('Machinist Calculator')
        self._grid = tk.Grid()
        self._num_rows = 9
        self._num_cols = 4
        self._calc = Calculator(self._root)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self._close)
        self._set_cell_size()
    
    def _redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def _wait_for_close(self):
        self._running = True

        while self._running:
            self._redraw()

    def _close(self):
        self._running = False

    def _set_cell_size(self):
        for i in range(self._num_rows):
            self._root.rowconfigure(index=i, minsize=100)
        for i in range(self._num_cols):
            self._root.columnconfigure(index=i, minsize=100)

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