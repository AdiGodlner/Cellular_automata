from CellConfigMSG import CellConfigMSG


from Cell import Cell


class Sea(Cell):

    def __init__(self):
        super().__init__("blue", "S")
        self.height = 0  # sea starts at sea level ?

    def update(self, configuration):
        pass

    def calcUpdate(self, neighbors):
        return CellConfigMSG(type(self), self.height, self.temperature, self.clouds, self.wind)
