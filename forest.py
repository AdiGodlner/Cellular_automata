from configs import ForestConfig, LAND_NAME
from cell import Cell
from wind import RAIN


class Forest(Cell):

    def __init__(self, config: ForestConfig):
        # super().__init__("Forest", height, temperature, wind, , "F")
        super().__init__(config)

    def copy(self):
        return Forest(self.config.copy())

    def calcUpdate(self, neighborhood):

        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)

        if new_config.temperature > self.config.fireThreshold:
            # if temprature exceeded fireThreshold the forest burns down to a Land tile
            new_config.name = LAND_NAME
            wind.pollution += 1  # forest fire adds to the pollution
        elif self.config.wind.pollution > self.config.acidRainThreshold and self.config.wind.clouds == RAIN:
            new_config.name = LAND_NAME
        else:
            new_config.name = self.config.name

        # if the cell should not change type (i.e. did not burn down ) then we remove some pollution from the air
        if wind.pollution != 0 and new_config.name == self.config.name:
            wind.pollution -= self.config.pollutionRemovalRate

        new_config.wind = wind

        return new_config
