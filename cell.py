from wind import *
from configs import CellConfig

# seasons
WINTER = "WINTER"
SPRING = "SPRING"
SUMMER = "SUMMER"
AUTUMN = "AUTUMN"


class Cell:

    def __init__(self, cellConfig):
        self.config = cellConfig  # a ticking clock that goes between 0 and 100 to vary temperature by season

    def update(self, configuration: CellConfig):
        self.config.time += 1
        self.config.temperature = configuration.temperature
        self.config.wind = configuration.wind
        # wind:{self.wind}\n clouds{'C' if self.wind.clouds else '_'}
        self.config.text = self.get_text()

    def calcUpdate(self, neighbors):
        pass

    def calcTemperature(self, neighborhood):

        pollutionTempIncrease = 1 + (self.config.wind.pollution / 100)
        runningTemp = self.config.temperature
        neighborsCount = 1

        # for row in neighborhood:
        #     for cell in row:
        #         if cell is not None:
        #             neighborsCount += 1
        #             runningTemp += cell.config.temperature

        temprature = int(runningTemp * pollutionTempIncrease) // neighborsCount
        temprature += self.getTempratureSeasonChange()

        return temprature

    def calcWind(self, neighborhood):

        upWind = 0
        leftWind = 0
        incoming_clouds = []
        pollution = 0
        # honestly doing this in a loop is more complicated than unfurling the loop, so I have unfurled it
        # get relevant neighbors
        aboveNeighbor = neighborhood[0][1]
        belowNeighbor = neighborhood[2][1]
        leftNeighbor = neighborhood[1][0]
        rightNeighbor = neighborhood[1][2]

        # only add the winds that point to this tile
        if aboveNeighbor.config.wind.direction == DOWN:
            upWind -= self.calc_incoming_wind_speed(aboveNeighbor)
            incoming_clouds.append(aboveNeighbor.config.wind.clouds)
            pollution += aboveNeighbor.config.wind.pollution

        if belowNeighbor.config.wind.direction == UP:
            upWind += self.calc_incoming_wind_speed(belowNeighbor)
            incoming_clouds.append(belowNeighbor.config.wind.clouds)
            pollution += belowNeighbor.config.wind.pollution

        if leftNeighbor.config.wind.direction == RIGHT:
            leftWind -= self.calc_incoming_wind_speed(leftNeighbor)
            incoming_clouds.append(leftNeighbor.config.wind.clouds)
            pollution += leftNeighbor.config.wind.pollution

        if rightNeighbor.config.wind.direction == LEFT:
            leftWind += self.calc_incoming_wind_speed(rightNeighbor)
            incoming_clouds.append(rightNeighbor.config.wind.clouds)
            pollution += leftNeighbor.config.wind.pollution

        clouds = self.calc_incoming_clouds(incoming_clouds)

        windSpeed = int(max(abs(upWind), abs(leftWind)))
        windDirection = self.calc_wind_direction(upWind, leftWind)
        return Wind(windDirection, windSpeed, pollution, clouds)

    def calc_wind_direction(self, upWind, leftWind):

        windDirection = None

        if abs(upWind) > abs(leftWind):
            windDirection = "UP" if upWind > 0 else "DOWN"
        else:
            windDirection = "LEFT" if upWind > 0 else "RIGHT"
        windDirection = self.seasonWindChange(windDirection)

        return windDirection

    def seasonWindChange(self, windDirection):
        windDirectionIndex = WIND_DIRECTIONS.index(windDirection)
        seasonChange = self.checkSeasonChange()
        if seasonChange is None:
            return windDirection
        elif seasonChange == WINTER:
            windDirectionIndex += 1
        elif seasonChange == SPRING:
            windDirectionIndex += 2
        elif seasonChange == SUMMER:
            windDirectionIndex += 3
        elif seasonChange == AUTUMN:
            windDirectionIndex += 3

        windDirectionIndex = windDirectionIndex % 4
        return WIND_DIRECTIONS[windDirectionIndex]

    def getTempratureSeasonChange(self):
        seasonChange = self.checkSeasonChange()
        if seasonChange is None:
            return 0
        elif seasonChange == WINTER:
            return -10
        elif seasonChange == SPRING:
            return 5
        elif seasonChange == SUMMER:
            return 10
        elif seasonChange == AUTUMN:
            return -5

    def checkSeasonChange(self):
        if self.config.time == 0:
            return WINTER
        elif self.config.time == 25:
            return SPRING
        elif self.config.time == 50:
            return SUMMER
        elif self.config.time == 75:
            return AUTUMN
        else:
            return None

    def calc_incoming_wind_speed(self, other):
        wind_speedup = other.config.height - self.config.height
        return other.config.wind.speed + wind_speedup

    def calc_incoming_clouds(self, incoming_clouds):

        cloudCount = 0
        rainCount = 0

        # stop raining in the next turn if it rained in the current state of this cell
        if self.config.wind.clouds == RAIN:
            cloudCount += 1
        # calculate clouds coming from other cells
        for incoming_cloud in incoming_clouds:
            if incoming_cloud == RAIN:
                rainCount += 1
                cloudCount += 1
            elif incoming_cloud == CLOUDY:
                cloudCount += 1

        if rainCount > 1:
            return RAIN
        elif cloudCount > 1:
            return RAIN if self.config.temperature < 15 else CLOUDY
        else:
            return NO_CLOUDS

    def get_text(self):
        return (f"Temp: {self.config.temperature}\n"
                f"Type: {self.config.name}\n"
                f"Wind: {self.config.wind.speed}\n"
                f"Poll: {self.config.wind.pollution}\n"
                f"WindDirection: {self.config.wind.direction}\n"
                f"Clouds: {self.config.wind.clouds}\n"
                )
