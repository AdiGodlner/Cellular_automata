from configs import ForestConfig, LAND_NAME
from cell import Cell
from wind import RAIN


class Forest(Cell):
    """
    Represents a forest cell in the cellular automata simulation

    :param config: (ForestConfig) The configuration for the forest cell.
    Methods:
         copy(self): Creates a deep copy of the forest cell
         calcUpdate(self, neighborhood): Calculates and returns the updated configuration for the next time step

    """
    def __init__(self, config: ForestConfig):
        super().__init__(config)

    def copy(self):
        """
            Creates a deep copy of the cell
            :return: A new instance of the City cell with the same configuration
        """
        return Forest(self.config.copy())

    def calcUpdate(self, neighborhood):
        """
        Calculates the next state of the forest cell based on its current state and neighborhood

        :param neighborhood: (list of lists) The neighborhood of the forest cell
        :return: ForestConfig: The updated configuration object for the forest cell
        """
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature()
        wind = self.calcWind(neighborhood)
        # change wind direction when hitting a forest because wind direction needs to change somewhere
        wind.direction = self.skewWindDirection(wind.direction, 1)

        if new_config.temperature > self.config.fireThreshold:
            # if temprature exceeded fireThreshold the forest burns down to a Land tile
            new_config.name = LAND_NAME
            wind.pollution += 1  # forest fire adds to the pollution
        elif self.config.wind.pollution > self.config.acidRainThreshold and self.config.wind.clouds == RAIN:
            new_config.name = LAND_NAME
        else:
            new_config.name = self.config.name

        # if the cell should not change type (i.e. did not burn down ) then we remove some pollution from the air
        if wind.pollution > -4 and new_config.name == self.config.name:
            wind.pollution -= self.config.pollutionRemovalRate

        new_config.wind = wind

        return new_config
