import tkinter as tk
from typing import List
import Cell
import CellConfigMSG
from Sea import Sea
from Forest import Forest
from IceBerg import IceBerg
from City import City
from Land import Land
import random
import time

# constants #TODO maybe this should be in if name == main
LAND_P = 0.14
CITY_P = 0.07
FOREST_P = 0.06
SEA_P = 0.7
ICEBERG_P = 0.03


def random_cell():
    # Randomly choose a cell type (e.g., Land , Sea, Ice )
    options = [Land, City, Forest, Sea, IceBerg]
    probabilities = [LAND_P, CITY_P, FOREST_P, SEA_P, ICEBERG_P]  # Adjust these probabilities as needed

    cell_type = random.choices(options, weights=probabilities, k=1)[0]

    # Create an instance of the chosen cell type
    return cell_type()


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
        # self.green_board = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]
        self.green_board = [[random_cell() for _ in range(width)] for _ in range(height)]
        self.blue_board = deep_copy(self.green_board)
        self.curr_board = "green"

        self.average_temperature = 0
        self.average_temperature_label = tk.Label(self.window, text="Average Temperature: N/A")
        self.average_temperature_label.pack()

    def draw_board(self):
        self.canvas.delete("grid")

        board = self.get_active_board()

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
                                        font=("Arial", font_size, "bold"))

        # redraw average temperature
        self.average_temperature_label.config(text=f"Average Temperature: {self.average_temperature}")

    def update_board(self):

        background_board = self.get_background_board()
        foo = background_board[0]
        bar = background_board[0][0]
        active_board = self.get_active_board()
        totalTmep = 0

        for i in range(self.height):
            for j in range(self.width):
                # get current cell and its neighbors
                currCell = active_board[i][j]
                neighborhood = self.get_neighborhood(i, j)
                # calculate the current cell configuration for next time step
                cellConfigMSG = currCell.calcUpdate(neighborhood)

                # get background board cell and set its configuration to the next time curr cell config
                background_cell = background_board[i][j]
                background_cell.update(cellConfigMSG)

                # calculate average temperature of board
                totalTmep += currCell.temperature

        self.average_temperature = totalTmep / (self.height * self.width)
        # switch active board
        self.curr_board = "blue" if self.curr_board == "green" else "green"

    def get_neighborhood(self, row, col):

        neighborhood = []
        board = self.get_active_board()

        for i in range(-1, 2):
            newRow = []
            neighborhood.append(newRow)

            neighbor_row = row + i

            # make graph spherical by making rows circular
            if neighbor_row < 0:
                neighbor_row = self.height - 1
            elif neighbor_row == self.height:
                neighbor_row = 0

            for j in range(-1, 2):

                if i == 0 and j == 0:
                    # current knows it's in its own neighborhood so there is no need to add itself to the
                    # neighborhood matrix, so we add None instead and skip other logic in the loop
                    newRow.append(None)
                    continue

                neighbor_col = col + j
                # make graph spherical by making columns circular
                if neighbor_col < 0:
                    neighbor_col = self.width - 1
                elif neighbor_col == self.width:
                    neighbor_col = 0

                newRow.append(board[neighbor_row][neighbor_col])

        return neighborhood

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

        newRow = []
        boardCopy.append(newRow)

        for j in range(len(board[0])):
            # create a new list by copying the elements of each row
            newRow.append(board[i][j].copy())

    return boardCopy


if __name__ == '__main__':
    #  TODO remember in documentation and read me there is a need to install tkinter
    # and or make into an exe

    _width, _height = 10, 10
    _cell_size = 70

    game = CA(_width, _height, _cell_size)
    game.start_game()
    # window.mainloop() # what is that and what does it do

    # canvas = tk.Canvas(window, bg="black")
    # canvas.pack()
    # canvas.create_rectangle((50,20,10,10),fill="red")
