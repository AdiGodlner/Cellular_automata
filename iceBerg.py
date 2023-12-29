from configs import IceBergConfig, SEA_NAME
from cell import Cell


class IceBerg(Cell):
    """
    Represents an iceBerg cell in the cellular automata simulation

    :param config: (IceBergConfig) The configuration for the iceBerg cell.
    Methods:
         copy(self): Creates a deep copy of the iceBerg cell
         calcUpdate(self, neighborhood): Calculates and returns the updated configuration for the next time step

    """
    def __init__(self, config: IceBergConfig):
        super().__init__(config)

    def copy(self):
        """
            Creates a deep copy of the cell
            :return: A new instance of the City cell with the same configuration
        """
        return IceBerg(self.config.copy())

    def calcUpdate(self, neighborhood):
        """
        Calculates the next state of the cell based on its current state and neighborhood

        :param neighborhood: (list of lists) The neighborhood of the iceBerg cell
        :return: IceBergConfig: The updated configuration for the cell
        """
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature()
        wind = self.calcWind(neighborhood)
        wind.direction = self.skewWindDirection(wind.direction, 3)
        new_config.wind = wind

        if self.config.temperature > self.config.meltThreshold:
            # above meltThreshold icebergs melt
            new_config.name = SEA_NAME

        return new_config
