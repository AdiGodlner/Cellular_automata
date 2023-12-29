from tkinter import ttk
import tkinter as tk


class CellularAutomataBoardViewer(ttk.Frame):
    """
    The GUI element for displaying the cellular automata board.

    Important attributes:
        cellularAutomata (CellularAutomata): The cellular automata instance for simulation
        board_view (list of lists of ttk.Label): 2D list containing labels representing cells on the board
    """
    def __init__(self, parent, cellularAutomata, columns, rows, cell_size):
        super().__init__(parent)
        self.cellularAutomata = cellularAutomata
        # create scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.on_scroll)
        self.scrollbar.pack(side="right", fill="y")
        # create the canvas that displays the cells and bind canvas to scrollbar
        self.canvas = tk.Canvas(self, width=columns * 1000, height=rows * 1000, borderwidth=0,
                                highlightthickness=0, yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.board_view = self.initialize_board_view()

    def on_canvas_configure(self, event):
        """
        Configures the canvas scroll
        :param event: ignore   we must accept event as parameter because tkinter sends it even do we do not use it
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_scroll(self, *args):
        """    Handles scrolling events for the canvas """
        self.canvas.yview(*args)

    def initialize_board_view(self):
        """
        Initializes the board view with labels representing cells on the board
        :return: The 2D list of ttk.Label representing cells on the board.
        """
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

    def draw_cell(self, row, column, text, color):
        """
        Updates the label for the specified cell with new text and color.

        :param row: The row index of the cell
        :param column: The column index of the cell
        :param text: The new text for the cell
        :param color: The new background color for the cell
        """
        self.board_view[row][column].config(text=text, font=("Arial", 12), background=color)
