from CellConfigMSG import CellConfigMSG
from Cell import Cell


class IceBerg(Cell):

    def __init__(self):
        super().__init__("white", "I")

    def update(self, neighbors):
        pass

    def calcUpdate(self, neighbors):
        return CellConfigMSG(type(self), self.height, self.temperature, self.clouds, self.wind)
