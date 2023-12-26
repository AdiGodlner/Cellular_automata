import tkinter as tk
from tkinter import ttk


class CellularAutomataViewer(ttk.Frame):

    def __init__(self, parent, cellularAutomata, columns, rows, cell_size):
        super().__init__(parent)
        self.cellularAutomata = cellularAutomata
        self.columns = columns
        self.rows = rows
        self.cell_size = cell_size
        self.canvas = tk.Canvas(self, width=columns * cell_size, height=rows * cell_size, borderwidth=0,
                                highlightthickness=0)
        self.canvas.grid(row=rows, column=columns, sticky='nsew')
        self.board_view = self.initialize_board_view()
        self.average_temperature_label = ttk.Label(self, text="Average Temperature: N/A")
        # self.average_temperature_label.pack()

    def create_layout(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def initialize_board_view(self):

        board_view = []
        ca_board = self.cellularAutomata.get_active_board()
        for i, ca_row in enumerate(ca_board):

            board_view_row = []
            board_view.append(board_view_row)
            for j, cell in enumerate(ca_row):
                # Create a Label
                label = ttk.Label(self.canvas, text=cell.get_text(),
                                  font=("Arial", 12), background=cell.config.color,
                                  padding=0)
                label.grid(row=i, column=j)
                # save vars to board_view
                board_view_row.append(label)
                self.canvas.grid_rowconfigure(i, weight=1, uniform="board")
                self.canvas.grid_columnconfigure(j, weight=1, uniform="board")

        return board_view

    def draw_board(self):

        board = self.cellularAutomata.get_active_board()

        for i, view_row in enumerate(self.board_view):
            for j, cell_label in enumerate(view_row):
                currCell = board[i][j]
                cell_label.config(text=currCell.get_text(), font=("Arial", 12), background=currCell.config.color)

        # redraw average temperature
        self.average_temperature_label.config(text=f"Average Temperature: {self.cellularAutomata.average_temperature}")
