import tkinter as tk
from tkinter import ttk
import sys
import Board
from Sudoku import runSolver
from Sudoku import nextRC

class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert(tk.END,str)

class Sudoku(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.parent.title("Sudoku Solver")
        self.menus = []
        self.createWidgets()

    def createWidgets(self):
        canvas=tk.Canvas(self.parent, width=500, height=300)
        canvas.grid(row=1, column=1)

        #self.createMenus(canvas)
        self.createEntries(canvas)
        self.createSeparators(canvas)
        
        solveButton = tk.Button(canvas, text="Solve", command=lambda: self.startSolver())
        solveButton.grid(row=11, column=5)

        output = tk.Text(self.parent)
        output.grid(row=2, column=1)
        sys.stdout = StdoutRedirector(output)
    
    def createEntries(self, canvas):
        for r in range(1, 10):
            for c in range(1, 10):
                temp = tk.Entry(canvas, width=7, justify=tk.CENTER)
                temp.grid(row=r, column=c, padx=2, pady=6)
                self.menus.append(temp)

    def createMenus(self, canvas):
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]
        for r in range(1, 10):
            for c in range(1, 10):
                temp = tk.StringVar()
                temp.set("X")
                tempMenu = tk.OptionMenu(canvas, temp, *options)
                tempMenu.grid(row=r, column=c)
                self.menus.append(temp)
    
    def createSeparators(self, canvas):
        line_style = ttk.Style()
        line_style.configure("Line.TSeparator", background="#000000")
        #for y in range(95, 200, 96):
        for y in range(92, 200, 93):
            separator = ttk.Separator(canvas, orient='horizontal', style="Line.TSeparator")
            separator.place(x=1, y=y, relwidth=1)
        #for x in range(155, 400, 156):
        for x in range(149, 400, 150):
            separator = ttk.Separator(canvas, orient='vertical', style="Line.TSeparator")
            separator.place(x=x, y=6, relheight=0.871)
    
    def createMenuMap(self):
        r = 0
        c = 0
        menuMap = {}
        for i in range(len(self.menus)):
            menuMap[i] = ((r, c))
            r, c = nextRC(r, c)
        return menuMap

    def startSolver(self):
        b = Board.Board()
        menuMap = self.createMenuMap()
        possibleNumbers = "123456789"
        for i in range(len(self.menus)):
            menu = self.menus[i]
            #if menu.get() != "X":
            if menu.get() in possibleNumbers and menu.get() != "":
                b.setNumberWithTag(menuMap[i][0], menuMap[i][1], int(menu.get()))
        runSolver(b)

def runGUI():
    root = tk.Tk()
    frame = Sudoku(root)
    frame.grid()
    root.mainloop()
    sys.stdout = sys.__stdout__

runGUI()
    
