import tkinter as tk

import random
import time


class CA:
    def __init__(self, width, height, cell_size=20):
        self.window = tk.Tk()
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.canvas = tk.Canvas(self.window, width=width * cell_size, height=height * cell_size, borderwidth=0,
                                highlightthickness=0)
        self.canvas.pack()

        # randomize board for game of life
        self.green_board = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]
        self.blue_board = deep_copy(self.green_board)
        self.curr_board = "green"

    def draw_board(self):
        self.canvas.delete("all")

        board = self.get_active_board()

        for i in range(self.height):
            for j in range(self.width):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                color = "black" if board[i][j] == 1 else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray", fill=color)

    def update_board(self):
        #  TODO update board with info of CA rules

        background_board = self.get_background_board()
        active_board = self.get_active_board()

        for i in range(self.height):
            for j in range(self.width):
                neighbors = self.count_neighbors(i, j)
                if active_board[i][j] == 1:
                    background_board[i][j] = 1 if 2 <= neighbors <= 3 else 0
                else:
                    background_board[i][j] = 1 if neighbors == 3 else 0

        # switch active board
        self.curr_board = "blue" if self.curr_board == "green" else "green"

    def count_neighbors(self, row, col):

        count = 0
        board = self.get_active_board()

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor_row, neighbor_col = row + i, col + j
                if 0 <= neighbor_row < self.height and 0 <= neighbor_col < self.width:
                    count += board[neighbor_row][neighbor_col]
        return count

    def start_game(self, generations=100):
        for _ in range(generations):
            self.draw_board()
            self.update_board()
            self.window.update()
            time.sleep(0.1)

    def get_active_board(self):
        return self.green_board if self.curr_board == "green" else self.blue_board

    def get_background_board(self):
        return self.green_board if self.curr_board != "green" else self.blue_board


def deep_copy(board):
    """
    creates a deep copy of a 2D board.
    :param board: (list of lists) the original 2D board to be copied
    :return: (list of lists) a new 2D board that is a deep copy of the original
    """
    boardCopy = []
    # iterate through the rows of the original board
    for i in range(len(board)):
        # create a new list by copying the elements of each row
        boardCopy.append(board[i].copy())
    return boardCopy


if __name__ == '__main__':
    #  TODO remember in documentation and read me there is a need to install tkinter
    # and or make into an exe

    width, height = 30, 20
    cell_size = 20

    game = CA(width, height, cell_size)
    game.start_game()
    # window.mainloop() # what is that and what does it do

    # canvas = tk.Canvas(window, bg="black")
    # canvas.pack()
    # canvas.create_rectangle((50,20,10,10),fill="red")
