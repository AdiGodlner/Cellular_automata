from wind import Wind, randomWind


class Cell:

    def __init__(self, height, temperature, wind, color, text):
        self.height = height
        self.temperature = temperature
        self.wind = wind
        self.text = text
        self.color = color
        self.time = 0  # a ticking clock that goes between 0 and 100 to vary temperature by season

    def update(self, configuration):
        self.time += 1
        self.temperature = configuration.temperature
        self.wind = configuration.wind
        # wind:{self.wind}\n clouds{'C' if self.wind.clouds else '_'}
        self.text = f"T:{self.temperature}\n  "

    def calcUpdate(self, neighbors):
        pass

    def calcTemperature(self, neighborhood):

        pollutionTempIncrease = 1 + (self.wind.pollution / 100)
        runningTemp = self.temperature
        neighborsCount = 0

        for row in neighborhood:
            for cell in row:
                if cell is not None:
                    neighborsCount += 1
                    runningTemp += cell.temperature

        # TODO add calculation by season

        return (runningTemp * pollutionTempIncrease) // (neighborsCount + 1)

    def calcWind(self, neighborhood):

        upWind = 0
        leftWind = 0
        clouds = False
        pollution = 0
        windDirection = ""
        # honestly doing this in a loop is more complicated than unfurling the loop, so I have unfurled it
        # get relevant neighbors
        aboveNeighbor = neighborhood[0][1]
        belowNeighbor = neighborhood[2][1]
        leftNeighbor = neighborhood[1][0]
        rightNeighbor = neighborhood[1][2]

        # only add the winds that point to this tile
        if aboveNeighbor.wind.direction == "DOWN":
            upWind -= aboveNeighbor.wind.speed
            clouds = clouds or aboveNeighbor.wind.clouds
            pollution += aboveNeighbor.wind.pollution

        if belowNeighbor.wind.direction == "UP":
            upWind += belowNeighbor.wind.speed
            clouds = clouds or belowNeighbor.wind.clouds
            pollution += belowNeighbor.wind.pollution

        if leftNeighbor.wind.direction == "RIGHT":
            leftWind -= leftNeighbor.wind.speed
            clouds = clouds or leftNeighbor.wind.clouds
            pollution += leftNeighbor.wind.pollution

        if rightNeighbor.wind.direction == "LEFT":
            leftWind += rightNeighbor.wind.speed
            clouds = clouds or rightNeighbor.wind.clouds
            pollution += leftNeighbor.wind.pollution

        # TODO add self? clouds pollution wind
        # TODO wind should change based on time

        if abs(upWind) > abs(leftWind):
            windDirection = "UP" if upWind > 0 else "DOWN"
        else:
            windDirection = "LEFT" if upWind > 0 else "RIGHT"

        return Wind(windDirection, max(abs(upWind), abs(leftWind)), pollution, clouds)
