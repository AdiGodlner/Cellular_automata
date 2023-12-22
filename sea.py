from cellConfigMSG import CellConfigMSG

from cell import Cell


class Sea(Cell):

    def __init__(self, height, temperature, wind):
        # sea starts at sea level = 0 ?
        super().__init__(height, temperature, wind, "blue", "S")

    def copy(self):
        return Sea(self.height, self.temperature, self.wind.copy())

    def calcUpdate(self, neighborhood):
        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)

        return CellConfigMSG(type(self), self.height, temperature, wind)
