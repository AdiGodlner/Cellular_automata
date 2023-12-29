import random

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

WIND_DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

RAIN = "Rain"
CLOUDY = "Cloudy"
NO_CLOUDS = "NO_CLOUDS"
CLOUDS_STATES = [RAIN, CLOUDY, NO_CLOUDS]


def randomWind(pollution):
    """
    Generate a random wind

    :param pollution: (int) The wind's pollution .
    :return: (Wind) A Wind object with random attributes.
    """
    return Wind(random.choice(WIND_DIRECTIONS), random.randint(0, 35), pollution, random.choice(CLOUDS_STATES))


class Wind:
    """
    Represents the wind in the cellular automata simulation
    """
    def __init__(self, direction, speed, pollution, clouds):
        self.direction = direction
        self.speed = speed
        self.pollution = pollution
        self.clouds = clouds

    def copy(self):
        """
        Create a copy of the current Wind object

        :return: (Wind) A new Wind object that is a copy of self
        """
        return Wind(self.speed, self.direction, self.pollution, self.clouds)
