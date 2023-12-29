from wind import *
from configs import CellConfig

# seasons
WINTER = "WINTER"
SPRING = "SPRING"
SUMMER = "SUMMER"
AUTUMN = "AUTUMN"


class Cell:
    """
     Represents a cell in the cellular automata simulation

     Attributes:
     - config (CellConfig): Configuration object holding all attributes of the cell
     """

    def __init__(self, cellConfig):
        self.config = cellConfig  # a ticking clock that goes between 0 and 100 to vary temperature by season

    def update(self, configuration: CellConfig):
        """
        Update the cell with a new configuration
        :param configuration: (CellConfig): New configuration for the cell
        """

        if self.config.time < 100:
            self.config.time += 1
        else:
            self.config.time = 0

        self.config.temperature = configuration.temperature
        self.config.wind = configuration.wind
        self.config.text = self.get_text()

    def calcUpdate(self, neighborhood):
        """
        Abstract method that should be implemented by all of its subClasses
        calculate the next configuration of the cell based on its neighbors

        :param neighborhood: List representing the cell's neighborhood

        :returns CellConfig: New configuration for the cell.
        """

        pass

    def calcTemperature(self):
        """
        Calculate the temperature of the cell
         considering pollution and seasonal changes

        :returns int: The calculated temperature
        """
        temprature = int(self.config.temperature + (self.config.wind.pollution / 10))
        temprature += self.getTempratureSeasonChange()

        return temprature

    def calcWind(self, neighborhood):
        """
        Calculate the wind configuration of the cell based on its neighbors

        :param neighborhood: List representing the cell's neighborhood

        :returns Wind: The new wind configuration for the cell
        """
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

        # hard cap negative pollution at -5
        if pollution < -5:
            pollution = -5

        clouds = self.calc_incoming_clouds(incoming_clouds)

        windSpeed = int(max(abs(upWind), abs(leftWind)))
        windDirection = self.calc_wind_direction(upWind, leftWind)
        return Wind(windDirection, windSpeed, pollution, clouds)

    def calc_wind_direction(self, upWind, leftWind):
        """
        Calculate the wind direction based on the incoming winds from neighbors

        :param upWind: The total incoming wind from above and below
        :param leftWind: The total incoming wind from the left and right

        :returns str: The calculated wind direction
        """
        if abs(upWind) > abs(leftWind):
            windDirection = "UP" if upWind > 0 else "DOWN"
        else:
            windDirection = "LEFT" if upWind > 0 else "RIGHT"
        windDirection = self.seasonWindChange(windDirection)

        return windDirection

    def seasonWindChange(self, windDirection):
        """
        Change the wind direction based on seasonal changes

        :param windDirection: The current wind direction

        :returns str: The new wind direction.
        """
        seasonChange = self.checkSeasonChange()
        if seasonChange is None:
            return windDirection
        else:
            return self.skewWindDirection(windDirection, 1)

    def skewWindDirection(self, windDirection, skewIndex):
        """
        Change the wind direction based on the skew index

        :param windDirection: The current wind direction
        :param skewIndex: The amount by which to skew the wind direction

        :returns str: The new wind direction
        """
        windDirectionIndex = WIND_DIRECTIONS.index(windDirection) + skewIndex
        windDirectionIndex = windDirectionIndex % 4
        return WIND_DIRECTIONS[windDirectionIndex]

    def getTempratureSeasonChange(self):
        """
        Get the temperature change based on seasonal changes

        :returns int: The temperature change.
        """
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
        """
        Check if a seasonal change has occurred and return the new season

        :returns str or None: The new season
        """
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

    def getSeason(self):
        """
            Get current season based on current cell's time

            :returns str or None: The current season
        """

        if self.config.time < 25:
            return WINTER
        elif self.config.time < 50:
            return SPRING
        elif self.config.time < 75:
            return SUMMER
        elif self.config.time < 101:
            return AUTUMN
        else:
            return None

    def calc_incoming_wind_speed(self, other):
        """
        Calculate the incoming wind speed based on height differences
        between self and other cell
        :param
        - incoming_clouds: List of cloud states from neighboring cells.

        Returns:
        - str: The calculated cloud state ("Rain", "Cloudy", or "NO_CLOUDS").
        """
        wind_speedup = other.config.height - self.config.height
        return other.config.wind.speed + wind_speedup

    def calc_incoming_clouds(self, incoming_clouds):
        """
        Calculate the incoming cloud state based on neighbors

        Parameters:
        - incoming_clouds: List of cloud states from neighboring cells.

        Returns:
        - str: The calculated cloud state ("Rain", "Cloudy", or "NO_CLOUDS").
        """
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
                f"Poll: {self.config.wind.pollution:2f}\n"
                f"WindDirection: {self.config.wind.direction}\n"
                f"Clouds: {self.config.wind.clouds}\n"
                )
