from CellConfigMSG import CellConfigMSG
from Cell import Cell


class Land(Cell):

    def __init__(self):
        super().__init__("brown","L")

    def update(self, neighbors):
        pass

    def calcUpdate(self, neighbors):
        return CellConfigMSG(type(self), self.height, self.temperature, self.clouds, self.wind)
