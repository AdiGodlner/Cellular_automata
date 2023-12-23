import tkinter as tk
from tkinter import ttk


class CellularAutomataViewer(ttk.Frame):

    def __init__(self, parent, cellularAutomata, width, height, cell_size):
        super().__init__(parent)
        self.cellularAutomata = cellularAutomata
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas = tk.Canvas(self, width=width * cell_size, height=height * cell_size, borderwidth=0,
                                highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.average_temperature_label = tk.Label(self, text="Average Temperature: N/A")
        # self.average_temperature_label.pack()

    def create_layout(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def draw_board(self):
        self.canvas.delete("grid")

        board = self.cellularAutomata.get_active_board()

        for i in range(self.height):
            for j in range(self.width):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                currCell = board[i][j]
                color = currCell.color

                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray", fill=color, tags="grid")
                # Calculate the available space inside the rectangle
                available_width = x2 - x1
                available_height = y2 - y1

                # Choose a font size that fits the available space
                font_size = min(available_width // 2, available_height // 2)

                # Draw the text at the center of the rectangle
                # cloudsText = "C" if currCell.wind.clouds else "_"
                self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=currCell.text,
                                        font=("Arial", font_size))

        # redraw average temperature
        self.average_temperature_label.config(text=f"Average Temperature: {self.cellularAutomata.average_temperature}")
