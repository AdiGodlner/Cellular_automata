from land import Land
from city import City
from forest import Forest
from sea import Sea
from iceBerg import IceBerg
from wind import randomWind
from configs import *
from cell import Cell
import random


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
    def __init__(self, config: CellularAutomataConfig):
        # randomize board for game of life
        self.config = config
        self.green_board = [[self.random_cell() for _ in range(self.config.rows)] for _ in range(self.config.columns)]
        self.blue_board = board_copy(self.green_board)
        self.curr_board = "green"
        self.average_temperature = 0

    def random_cell(self):
        # Randomly choose a cell type (e.g., Land , Sea, Ice )
        options = [LAND_NAME, CITY_NAME, FOREST_NAME, SEA_NAME, ICEBERG_NAME]
        probabilities = self.config.cell_type_probabilities  # Adjust these probabilities as needed

        cell_name = random.choices(options, weights=probabilities, k=1)[0]
        height = random.uniform(self.config.min_height, self.config.max_height)
        temperature = self.getCellTempByName(cell_name)
        wind = randomWind(self.getStartingPollutionByCellName(cell_name))
        cellConfig = CellConfig(cell_name, height, temperature, wind.pollution,
                                wind.direction, wind.speed, wind.clouds, None, 0)
        # Create an instance of the chosen cell type
        return self.createCellByConfig(cellConfig)

    def getStartingPollutionByCellName(self, name):
        if name == FOREST_NAME:
            return self.config.forest_starting_pollution
        elif name == CITY_NAME:
            return self.config.city_starting_pollution
        elif name == ICEBERG_NAME:
            return self.config.iceBerg_starting_pollution
        elif name == LAND_NAME:
            return self.config.land_starting_pollution
        elif name == SEA_NAME:
            return self.config.sea_starting_pollution


    def createCellByConfig(self, cellConfig) -> Cell:
        name = cellConfig.name
        if name == FOREST_NAME:
            new_config = ForestConfig.fromCellConfig(cellConfig, self.config.pollutionRemovalRate,
                                                     self.config.fireThreshold, self.config.acidRainThreshold)
            return Forest(new_config)
        elif name == CITY_NAME:
            new_config = CityConfig.fromCellConfig(cellConfig, self.config.pollutionRemovalRate)
            return City(new_config)
        elif name == ICEBERG_NAME:
            new_config = IceBergConfig.fromCellConfig(cellConfig, self.config.meltThreshold)
            return IceBerg(new_config)
        elif name == LAND_NAME:
            new_config = LandConfig.fromCellConfig(cellConfig, self.config.forestThreshold)
            return Land(new_config)
        elif name == SEA_NAME:
            new_config = SeaConfig.fromCellConfig(cellConfig, self.config.makeCloudsThreshold)
            return Sea(new_config)

    def getCellTempByName(self, name):

        if name == FOREST_NAME:
            return random.uniform(self.config.forest_min_temp, self.config.forest_max_temp)
        elif name == CITY_NAME:
            return random.uniform(self.config.city_min_temp, self.config.city_max_temp)
        elif name == ICEBERG_NAME:
            return random.uniform(self.config.iceBerg_min_temp, self.config.iceBerg_max_temp)
        elif name == LAND_NAME:
            return random.uniform(self.config.land_min_temp, self.config.land_max_temp)
        elif name == SEA_NAME:
            return random.uniform(self.config.sea_min_temp, self.config.sea_max_temp)

    def update_board(self):

        background_board = self.get_background_board()
        active_board = self.get_active_board()
        totalTmep = 0

        for i in range(self.config.rows):
            for j in range(self.config.columns):
                # get current cell and its neighbors
                currCell = active_board[i][j]
                neighborhood = self.get_neighborhood(i, j)
                # calculate the current cell configuration for next time step
                cellConfigMSG = currCell.calcUpdate(neighborhood)

                # get background board cell and set its configuration to the next time curr cell config
                background_cell = background_board[i][j]
                if cellConfigMSG.name == background_cell.config.name:
                    background_cell.update(cellConfigMSG)
                else:
                    new_cell = self.createCellByConfig(cellConfigMSG)
                    new_cell.update(cellConfigMSG)
                    background_board[i][j] = new_cell
                # calculate average temperature of board
                totalTmep += currCell.config.temperature

        self.average_temperature = totalTmep / (self.config.rows * self.config.columns)
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
                neighbor_row = self.config.rows - 1
            elif neighbor_row == self.config.rows:
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
                    neighbor_col = self.config.columns - 1
                elif neighbor_col == self.config.columns:
                    neighbor_col = 0

                newRow.append(board[neighbor_row][neighbor_col])

        return neighborhood

    def get_active_board(self):
        return self.green_board if self.curr_board == "green" else self.blue_board

    def get_background_board(self):
        return self.green_board if self.curr_board != "green" else self.blue_board
