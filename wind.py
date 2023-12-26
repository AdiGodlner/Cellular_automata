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
    return Wind(random.choice(WIND_DIRECTIONS), random.randint(0, 35), pollution, random.choice(CLOUDS_STATES))


class Wind:

    def __init__(self, direction, speed, pollution, clouds):
        self.direction = direction
        self.speed = speed
        self.pollution = pollution
        self.clouds = clouds  # what are clouds # TODO initialize random cloud

    def copy(self):
        return Wind(self.speed, self.direction, self.pollution, self.clouds)
