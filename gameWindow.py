import tkinter as tk
from tkinter import ttk
from cellularAutomata import CellularAutomata
from cellularAutomataViewer import CellularAutomataViewer
import time


class GameWindow(tk.Tk):

    def __init__(self, width, height, cell_size):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cellularAutomata = CellularAutomata(width, height)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)
        label1 = ttk.Label(self, text="label1", background="red")
        label1.grid(row=0, column=0, sticky='nsew')
        self.cellularAutomataViewer = CellularAutomataViewer(self, self.cellularAutomata, width,
                                                             height,
                                                             cell_size)

        self.cellularAutomataViewer.grid(row=0, column=1, sticky='nsew')

    def start_game(self):
        self.play_round()
        self.mainloop()

    def play_round(self):
        self.cellularAutomataViewer.draw_board()
        self.cellularAutomata.update_board()
        self.update()
        self.after(1000, self.play_round)
