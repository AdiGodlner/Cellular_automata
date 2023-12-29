"""
Cellular Automata Configuration

This module defines classes for configuring the cellular automata simulation. It includes configurations for different types of cells, such as Forest, City, IceBerg, Land, and Sea.

Classes:
    - CellConfig: Base class for cell configurations.
    - ForestConfig: Configuration for Forest cells.
    - CityConfig: Configuration for City cells.
    - IceBergConfig: Configuration for IceBerg cells.
    - LandConfig: Configuration for Land cells.
    - SeaConfig: Configuration for Sea cells.
    - CellularAutomataConfig: Overall configuration for the cellular automata simulation.

Constants:
    - FOREST_NAME: Name for Forest cells.
    - CITY_NAME: Name for City cells.
    - ICEBERG_NAME: Name for IceBerg cells.
    - LAND_NAME: Name for Land cells.
    - SEA_NAME: Name for Sea cells.

Usage:
    CellularAutomataConfig is used to configure the simulation.
    for both the actual cellular automata and general
    configurations like the time between turns

    The other classes like ForestConfig, CityConfig, etc.
    are used to create cells of different types.

"""
from wind import Wind

# cellNames
FOREST_NAME = "Forest"
CITY_NAME = "City"
ICEBERG_NAME = "IceBerg"
LAND_NAME = "Land"
SEA_NAME = "Sea"


class CellConfig:

    def __init__(self, name, height, temperature, pollution
                 , windDirection, windSpeed, clouds, color, time):
        self.name = name
        self.height = height
        self.temperature = temperature
        self.wind = Wind(windDirection, windSpeed, pollution, clouds)
        self.color = color
        self.time = time  # a ticking clock that goes between 0 and 100 to vary temperature by season

    def copy(self):
        pass


class ForestConfig(CellConfig):

    def __init__(self, height, temperature, pollution
                 , windDirection, windSpeed, clouds,
                 time, pollutionRemovalRate, fireThreshold, acidRainThreshold):
        super().__init__(FOREST_NAME, height, temperature, pollution
                         , windDirection, windSpeed, clouds,
                         "green", time)
        self.pollutionRemovalRate = pollutionRemovalRate
        self.fireThreshold = fireThreshold
        self.acidRainThreshold = acidRainThreshold

    @staticmethod
    def fromCellConfig(cellConfig, pollutionRemovalRate, fireThreshold, acidRainThreshold):
        return ForestConfig(cellConfig.height, cellConfig.temperature,
                            cellConfig.wind.pollution, cellConfig.wind.direction,
                            cellConfig.wind.speed, cellConfig.wind.clouds,
                            cellConfig.time, pollutionRemovalRate, fireThreshold, acidRainThreshold)

    def copy(self):
        return ForestConfig(self.height, self.temperature, self.wind.pollution
                            , self.wind.direction, self.wind.speed,
                            self.wind.clouds, self.time, self.pollutionRemovalRate, self.fireThreshold
                            , self.acidRainThreshold)


class CityConfig(CellConfig):

    def __init__(self, height, temperature, pollution
                 , windDirection, windSpeed, clouds,
                 time, pollutionRate):
        super().__init__(CITY_NAME, height, temperature, pollution
                         , windDirection, windSpeed, clouds,
                         "grey", time)
        self.pollutionRate = pollutionRate

    @staticmethod
    def fromCellConfig(cellConfig, pollutionRate):
        return CityConfig(cellConfig.height, cellConfig.temperature,
                          cellConfig.wind.pollution, cellConfig.wind.direction,
                          cellConfig.wind.speed, cellConfig.wind.clouds,
                          cellConfig.time, pollutionRate)

    def copy(self):
        return CityConfig(self.height, self.temperature, self.wind.pollution
                          , self.wind.direction, self.wind.speed,
                          self.wind.clouds, self.time, self.pollutionRate)


class IceBergConfig(CellConfig):

    def __init__(self, height, temperature, pollution
                 , windDirection, windSpeed, clouds,
                 time, meltThreshold):
        super().__init__(ICEBERG_NAME, height, temperature, pollution
                         , windDirection, windSpeed, clouds,
                         "White", time)
        self.meltThreshold = meltThreshold

    @staticmethod
    def fromCellConfig(cellConfig, meltThreshold):
        return IceBergConfig(cellConfig.height, cellConfig.temperature,
                             cellConfig.wind.pollution, cellConfig.wind.direction,
                             cellConfig.wind.speed, cellConfig.wind.clouds,
                             cellConfig.time, meltThreshold)

    def copy(self):
        return IceBergConfig(self.height, self.temperature, self.wind.pollution
                             , self.wind.direction, self.wind.speed,
                             self.wind.clouds, self.time, self.meltThreshold)


class LandConfig(CellConfig):

    def __init__(self, height, temperature, pollution
                 , windDirection, windSpeed, clouds,
                 time, rainCount, forestThreshold):
        super().__init__(LAND_NAME, height, temperature, pollution
                         , windDirection, windSpeed, clouds,
                         "#bb805f", time)
        self.rainCount = rainCount
        self.forestThreshold = forestThreshold

    @staticmethod
    def fromCellConfig(cellConfig, forestThreshold):
        return LandConfig(cellConfig.height, cellConfig.temperature,
                          cellConfig.wind.pollution, cellConfig.wind.direction,
                          cellConfig.wind.speed, cellConfig.wind.clouds,
                          cellConfig.time, 0, forestThreshold)

    def copy(self):
        return LandConfig(self.height, self.temperature, self.wind.pollution
                          , self.wind.direction, self.wind.speed,
                          self.wind.clouds, self.time, self.rainCount, self.forestThreshold)


class SeaConfig(CellConfig):

    def __init__(self, height, temperature, pollution
                 , windDirection, windSpeed, clouds,
                 time, makeCloudsThreshold):
        super().__init__(SEA_NAME, height, temperature, pollution
                         , windDirection, windSpeed, clouds,
                         "#55d7e0", time)
        self.makeCloudsThreshold = makeCloudsThreshold

    @staticmethod
    def fromCellConfig(cellConfig, makeCloudsThreshold):
        return SeaConfig(cellConfig.height, cellConfig.temperature,
                         cellConfig.wind.pollution, cellConfig.wind.direction,
                         cellConfig.wind.speed, cellConfig.wind.clouds,
                         cellConfig.time, makeCloudsThreshold)

    def copy(self):
        return SeaConfig(self.height, self.temperature, self.wind.pollution
                         , self.wind.direction, self.wind.speed,
                         self.wind.clouds, self.time, self.makeCloudsThreshold)


class CellularAutomataConfig:

    def __init__(self
                 ,
                 # board configs
                 roundTimeMS,
                 rows,
                 columns,
                 # general configs
                 min_height,
                 max_height,

                 # city related configs
                 city_starting_pollution,
                 pollutionRate,
                 city_min_temp,
                 city_max_temp,

                 # forest related configs
                 forest_starting_pollution,
                 pollutionRemovalRate,
                 fireThreshold,
                 acidRainThreshold,
                 forest_min_temp,
                 forest_max_temp,

                 # land related configs
                 land_starting_pollution,
                 forestThreshold,
                 land_min_temp,
                 land_max_temp,

                 # iceBerg related configs
                 iceBerg_starting_pollution,
                 meltThreshold,
                 iceBerg_min_temp,
                 iceBerg_max_temp,

                 # sea related configs
                 sea_starting_pollution,
                 makeCloudsThreshold,
                 sea_min_temp,
                 sea_max_temp,

                 # cell type initialization probabilities
                 land_p,
                 city_p,
                 forest_p,
                 sea_p,
                 iceberg_p,

                 ):
        # board configs
        self.roundTimeMS = roundTimeMS
        self.rows = rows
        self.columns = columns
        # general configs
        self.min_height = min_height
        self.max_height = max_height

        # city related configs
        self.city_starting_pollution = city_starting_pollution
        self.pollutionRate = pollutionRate
        self.city_min_temp = city_min_temp
        self.city_max_temp = city_max_temp

        # forest related configs
        self.forest_starting_pollution = forest_starting_pollution
        self.pollutionRemovalRate = pollutionRemovalRate
        self.fireThreshold = fireThreshold
        self.acidRainThreshold = acidRainThreshold
        self.forest_min_temp = forest_min_temp
        self.forest_max_temp = forest_max_temp

        # land related configs
        self.land_starting_pollution = land_starting_pollution
        self.forestThreshold = forestThreshold
        self.land_min_temp = land_min_temp
        self.land_max_temp = land_max_temp

        # iceBerg related configs
        self.iceBerg_starting_pollution = iceBerg_starting_pollution
        self.meltThreshold = meltThreshold
        self.iceBerg_min_temp = iceBerg_min_temp
        self.iceBerg_max_temp = iceBerg_max_temp

        # sea related configs
        self.sea_starting_pollution = sea_starting_pollution
        self.makeCloudsThreshold = makeCloudsThreshold
        self.sea_min_temp = sea_min_temp
        self.sea_max_temp = sea_max_temp

        # cell type initialization probabilities
        self.land_p = land_p
        self.city_p = city_p
        self.forest_p = forest_p
        self.sea_p = sea_p
        self.iceberg_p = iceberg_p
        self.cell_type_probabilities = [self.land_p, self.city_p, self.forest_p, self.sea_p, self.iceberg_p]
