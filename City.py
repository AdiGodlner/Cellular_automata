from CellConfigMSG import CellConfigMSG
from Cell import Cell


class City(Cell):

    def __init__(self):
        super().__init__("grey", "C")

    def update(self, neighbors):
        pass

    def calcUpdate(self, neighbors):
        return CellConfigMSG(type(self), self.height, self.temperature, self.clouds, self.wind)
