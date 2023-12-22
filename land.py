from cellConfigMSG import CellConfigMSG
from cell import Cell


class Land(Cell):

    def __init__(self, height, temperature, wind):
        super().__init__(height, temperature, wind, "brown", "L")

    def copy(self):
        return Land(self.height, self.temperature, self.wind.copy())

    def calcUpdate(self, neighborhood):
        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)
        return CellConfigMSG(type(self), self.height, temperature, wind)
