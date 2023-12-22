import tkinter as tk
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
        self.cellularAutomataViewer = CellularAutomataViewer(self.window, self.cellularAutomata, width, height,
                                                             cell_size)

    def start_game(self, generations=100):
        for _ in range(generations):
            self.cellularAutomataViewer.draw_board()
            self.cellularAutomata.update_board()
            self.window.update()
            time.sleep(0.1)
