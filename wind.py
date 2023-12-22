import random

WIND_DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]


def randomWind():
    return Wind(random.choice(WIND_DIRECTIONS), random.randint(0, 35), 0, random.choice([True, False]))


class Wind:

    def __init__(self, direction, speed, pollution, clouds):
        self.direction = direction
        self.speed = speed
        self.pollution = pollution
        self.clouds = clouds  # what are clouds # TODO initialize random cloud

    def copy(self):
        return Wind(self.speed, self.direction, self.pollution, self.clouds)
