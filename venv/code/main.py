#!/usr/bin/env python 
import tkinter as tk
#from calc import Calculator


class Application():
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height
        self._root = tk.Tk()
        self._root.title('Machinist Calculator')
        self._canvas = tk.Canvas()
        self._canvas.pack()
        self._grid = tk.Grid()
#        self._calc = Calculator()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self._close)
    
    def _redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def _wait_for_close(self):
        self._running = True

        while self._running:
            self._redraw()

    def _close(self):
        self._running = False



app = Application(800, 600)
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