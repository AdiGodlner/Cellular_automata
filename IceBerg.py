from CellConfigMSG import CellConfigMSG
from Cell import Cell


class IceBerg(Cell):

    def __init__(self):
        super().__init__("white", "I")

    def copy(self):
        cellCopy = IceBerg()
        cellCopy.temperature = self.temperature
        cellCopy.wind = self.wind.copy()
        cellCopy.height = self.height
        return cellCopy

    def calcUpdate(self, neighborhood):
        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)

        return CellConfigMSG(type(self), self.height, temperature, wind)
