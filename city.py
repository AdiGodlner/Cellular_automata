import random

from cellConfigMSG import CellConfigMSG
from cell import Cell


class City(Cell):

    def __init__(self, height, temperature, wind):
        super().__init__(height, temperature, wind, "grey", "C")

    def copy(self):
        return City(self.height, self.temperature, self.wind.copy())

    def calcUpdate(self, neighborhood):
        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)
        # TODO generate pollution should there be a base pollution set by user
        return CellConfigMSG(type(self), self.height, temperature, wind)
