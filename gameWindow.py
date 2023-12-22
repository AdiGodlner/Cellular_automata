import tkinter as tk
from tkinter import ttk
from cellularAutomata import CellularAutomata
from cellularAutomataViewer import CellularAutomataViewer
import time


class GameWindow:

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.window = tk.Tk()
        self.cellularAutomata = CellularAutomata(width, height)

        self.cellularAutomataFrame = tk.Frame(self.window)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=2)
        self.window.rowconfigure(0, weight=1)
        label1 = ttk.Label(self.window, text="label1", background="red")
        label1.grid(row=0, column=0, sticky='nsew')
        self.cellularAutomataViewer = CellularAutomataViewer(self.cellularAutomataFrame, self.cellularAutomata, width,
                                                             height,
                                                             cell_size)

        self.cellularAutomataFrame.grid(row=0, column=1, sticky='nsew')

    def start_game(self, generations=100):
        for _ in range(generations):
            self.cellularAutomataViewer.draw_board()
            self.cellularAutomata.update_board()
            self.window.update()
            time.sleep(0.1)
