from configs import CityConfig
from cell import Cell


class City(Cell):
    """
     Represents a cell of type 'City' in the cellular automata simulation

     Attributes:
         config (CityConfig): The configuration settings for the City cell

     Methods:
         copy(self): Creates a deep copy of the City cell
         calcUpdate(self, neighborhood): Calculates and returns the updated configuration for the next time step

     """
    def __init__(self, config: CityConfig):
        super().__init__(config)

    def copy(self):
        """
        Creates a deep copy of the cell
        :return: A new instance of the City cell with the same configuration
        """
        return City(self.config.copy())

    def calcUpdate(self, neighborhood):
        """
        Calculates the next state of the city cell based on its current state and neighborhood

        :param neighborhood: The neighboring cells around the current City cell
        :return: The updated CityConfig for the next time step
        """
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature()
        new_config.wind = self.calcWind(neighborhood)
        new_config.wind.pollution += self.config.pollutionRate
        new_config.wind.direction = self.skewWindDirection(new_config.wind.direction, 1)

        return new_config
