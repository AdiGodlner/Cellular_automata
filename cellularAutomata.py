from land import Land
from city import City
from forest import Forest
from sea import Sea
from iceBerg import IceBerg
from wind import randomWind
import random
import time

# constants #TODO maybe this should be in if name == main
LAND_P = 0.14
CITY_P = 0.07
FOREST_P = 0.06
SEA_P = 0.7
ICEBERG_P = 0.03


def random_cell(min_height, max_height, min_temp, max_temp):
    # Randomly choose a cell type (e.g., Land , Sea, Ice )
    options = [Land, City, Forest, Sea, IceBerg]
    probabilities = [LAND_P, CITY_P, FOREST_P, SEA_P, ICEBERG_P]  # Adjust these probabilities as needed

    cell_type = random.choices(options, weights=probabilities, k=1)[0]
    height = random.uniform(min_height, max_height)
    temperature = random.uniform(min_temp, max_temp)
    wind = randomWind()
    # Create an instance of the chosen cell type
    return cell_type(height, temperature, wind)


def board_copy(board):
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


class CellularAutomata:
    def __init__(self, rows, columns):
        # randomize board for game of life
        self.rows = rows
        self.columns = columns
        self.green_board = [[random_cell(0, 10, 0, 100) for _ in range(rows)] for _ in range(columns)]
        self.blue_board = board_copy(self.green_board)
        self.curr_board = "green"

        self.average_temperature = 0

    def update_board(self):

        background_board = self.get_background_board()
        active_board = self.get_active_board()
        totalTmep = 0

        for i in range(self.rows):
            for j in range(self.columns):
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

        self.average_temperature = totalTmep / (self.rows * self.columns)
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
                neighbor_row = self.rows - 1
            elif neighbor_row == self.rows:
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
                    neighbor_col = self.columns - 1
                elif neighbor_col == self.columns:
                    neighbor_col = 0

                newRow.append(board[neighbor_row][neighbor_col])

        return neighborhood

    def get_active_board(self):
        return self.green_board if self.curr_board == "green" else self.blue_board

    def get_background_board(self):
        return self.green_board if self.curr_board != "green" else self.blue_board
