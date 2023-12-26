import tkinter as tk
from tkinter import ttk
from cellularAutomataViewer import CellularAutomataViewer


class GameWindow(tk.Tk):

    def __init__(self, rows, columns, cell_size, cellularAutomata):
        super().__init__()
        self.cell_size = cell_size
        self.cellularAutomata = cellularAutomata

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)
        label1 = ttk.Label(self, text="label1", background="red")
        label1.grid(row=0, column=0, sticky='nsew')
        self.cellularAutomataViewer = CellularAutomataViewer(self, self.cellularAutomata, rows,
                                                             columns,
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
