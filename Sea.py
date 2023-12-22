from CellConfigMSG import CellConfigMSG

from Cell import Cell


class Sea(Cell):

    def __init__(self):
        super().__init__("blue", "S")
        self.height = 0  # sea starts at sea level ?

    def copy(self):
        cellCopy = Sea()
        cellCopy.temperature = self.temperature
        cellCopy.wind = self.wind.copy()
        cellCopy.height = self.height
        return cellCopy

    def calcUpdate(self, neighborhood):
        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)

        return CellConfigMSG(type(self), self.height, temperature, wind)
