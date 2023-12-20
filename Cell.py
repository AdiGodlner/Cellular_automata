import CellConfigMSG

class Cell:

    def __init__(self, color, name):
        self.height = None
        self.temperature = None  # TODO initialize random temperature
        self.clouds = None  # what are clouds # TODO initialize random cloud
        # TODO should wind be an object since it contains polution speed and direction
        self.wind = None  # TODO initialize random wind
        self.name = name
        self.color = color

    def update(self, configuration):
        pass

    def calcUpdate(self, neighbors):
        pass