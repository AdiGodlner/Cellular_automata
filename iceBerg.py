from configs import  IceBergConfig, SEA_NAME
from cell import Cell


class IceBerg(Cell):

    def __init__(self, config: IceBergConfig):
        super().__init__(config)

    def copy(self):
        return IceBerg(self.config.copy())

    def calcUpdate(self, neighborhood):

        temperature = self.calcTemperature(neighborhood)
        wind = self.calcWind(neighborhood)
        new_config = self.config.copy()
        new_config.wind = wind
        new_config.temperature = temperature

        if self.config.temperature > self.config.meltThreshold:
            # above meltThreshold icebergs melt
            new_config.name = SEA_NAME

        return new_config
