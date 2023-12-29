import tkinter as tk
from cellularAutomataViewer import CellularAutomataViewer


class GameWindow(tk.Tk):
    """
    Represents the main game window for the cellular automata simulation.

    Attributes:
        cell_size (int): The size of each cell.
        cellularAutomata (CellularAutomata): The cellular automata instance for simulation.
        cellularAutomataViewer (CellularAutomataViewer): The viewer for displaying the cellular automata.
    """
    def __init__(self, rows, columns, cell_size, cellularAutomata):
        super().__init__()
        self.cell_size = cell_size
        self.cellularAutomata = cellularAutomata
        self.cellularAutomataViewer = CellularAutomataViewer(self, self.cellularAutomata, rows,
                                                             columns,
                                                             cell_size)

        self.cellularAutomataViewer.pack()

    def start_game(self):
        """
        Starts the cellular automata simulation.
        """
        self.play_round()
        self.mainloop()

    def play_round(self):
        """
              Plays a round of the cellular automata simulation.
              Draws the current state of the board, updates the cellular automata, and schedules the next round.
        """
        self.cellularAutomataViewer.draw_board()
        self.cellularAutomata.update_board()
        self.after(self.cellularAutomata.config.roundTimeMS, self.play_round)
