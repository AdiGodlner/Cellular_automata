from configs import SeaConfig
from cell import Cell
from wind import NO_CLOUDS, CLOUDY


class Sea(Cell):
    """
       Represents a sea cell in the cellular automata simulation

       :param config: (SeaConfig) The configuration for the sea cell.
       Methods:
            copy(self): Creates a deep copy of the land cell
            calcUpdate(self, neighborhood): Calculates and returns the updated configuration for the next time step

   """
    def __init__(self, config: SeaConfig):
        # sea starts at sea level = 0 ?
        super().__init__(config)

    def copy(self):
        """
           Creates a deep copy of the cell
           :return: A new instance of the City cell with the same configuration
        """
        return Sea(self.config.copy())

    def calcUpdate(self, neighborhood):
        """
        Calculates the next state of the cell based on its current state and neighborhood

        :param neighborhood: (list of lists) The neighborhood of the sea cell
        :return: LandConfig: The updated configuration for the cell
        """
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature()
        new_config.wind = self.calcWind(neighborhood)
        new_config.wind.speed += 1

        if new_config.wind.clouds == NO_CLOUDS and new_config.temperature > self.config.makeCloudsThreshold:
            new_config.wind.clouds = CLOUDY

        return new_config
