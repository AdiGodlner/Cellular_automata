from configs import CellConfig, LandConfig, FOREST_NAME
from cell import Cell
from wind import RAIN


class Land(Cell):

    def __init__(self, config: LandConfig):
        super().__init__(config)

    def copy(self):
        return Land(self.config.copy())

    def calcUpdate(self, neighborhood):
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature(neighborhood)
        new_config.wind = self.calcWind(neighborhood)
        if new_config.wind.clouds == RAIN:
            self.config.rainCount += 1
        if self.config.rainCount > self.config.forestThreshold:
            new_config.name = FOREST_NAME
        return new_config
