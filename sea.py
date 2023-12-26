from configs import SeaConfig
from cell import Cell
from wind import NO_CLOUDS , CLOUDY

class Sea(Cell):

    def __init__(self, config: SeaConfig):
        # sea starts at sea level = 0 ?
        super().__init__(config)

    def copy(self):
        return Sea(self.config.copy())

    def calcUpdate(self, neighborhood):
        new_config = self.config.copy()
        new_config.temperature = self.calcTemperature(neighborhood)
        new_config.wind = self.calcWind(neighborhood)
        if new_config.wind.clouds == NO_CLOUDS and new_config.temperature > self.config.makeCloudsThreshold:
            new_config.wind.clouds = CLOUDY

        return new_config
