import random

from configs import CityConfig
from cell import Cell


class City(Cell):

    def __init__(self, config: CityConfig):
        super().__init__(config)

    def copy(self):
        return City(self.config.copy())

    def calcUpdate(self, neighborhood):
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature(neighborhood)
        new_config.wind = self.calcWind(neighborhood)
        new_config.wind.pollution += self.config.pollutionRate

        return new_config
