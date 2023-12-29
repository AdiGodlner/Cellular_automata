from configs import LandConfig, FOREST_NAME
from cell import Cell
from wind import RAIN


class Land(Cell):
    """
       Represents a land cell in the cellular automata simulation

       :param config: (LandConfig) The configuration for the land cell.
       Methods:
            copy(self): Creates a deep copy of the land cell
            calcUpdate(self, neighborhood): Calculates and returns the updated configuration for the next time step

   """
    def __init__(self, config: LandConfig):
        super().__init__(config)

    def copy(self):
        """
           Creates a deep copy of the cell
           :return: A new instance of the City cell with the same configuration
        """
        return Land(self.config.copy())

    def calcUpdate(self, neighborhood):
        """
        Calculates the next state of the cell based on its current state and neighborhood

        :param neighborhood: (list of lists) The neighborhood of the land cell
        :return: LandConfig: The updated configuration for the cell
        """
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature()
        new_config.wind = self.calcWind(neighborhood)
        new_config.wind.speed += 1

        if new_config.wind.clouds == RAIN:
            self.config.rainCount += 1
        if self.config.rainCount > self.config.forestThreshold:
            new_config.name = FOREST_NAME
        return new_config
