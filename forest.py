from cellConfigMSG import CellConfigMSG
from cell import Cell


class Forest(Cell):

    def __init__(self, height, temperature, wind):
        super().__init__(height, temperature, wind, "green", "F")

    def copy(self):
        return Forest(self.height, self.temperature, self.wind.copy())

    def calcUpdate(self, neighborhood):
        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)

        return CellConfigMSG(type(self), self.height, temperature, wind)
