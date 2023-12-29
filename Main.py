from gameWindow import GameWindow
from configs import CellularAutomataConfig
from cellularAutomata import CellularAutomata
from stats import normalize_stats, plot, plotMinMaxAverage
import argparse
import json


def readCellularAutomataConfigFromFile(fileName):
    """
     Reads a CellularAutomataConfig object from a JSON file.

    :param fileName: (str) The name of the JSON file.
    :return: CellularAutomataConfig: The configuration object.
    """

    with open(fileName, 'r') as f:
        config = json.load(f)
    return CellularAutomataConfig(**config)


def getUserConfig():
    """
    Gets the name of the config file from the command line and creates a CellularAutomataConfig object.

    :return: CellularAutomataConfig: The configuration object.
    """
    # get the config file name
    parser = argparse.ArgumentParser(description='A program that presents a cellular automata')
    parser.add_argument('file_name', type=str, help='Cellular automata config file name')
    args = parser.parse_args()
    file_name = args.file_name

    return readCellularAutomataConfigFromFile(file_name)


if __name__ == '__main__':
    #  TODO remember in documentation and read me there is a need to install tkinter
    # and or make into an exe

    _cell_size = 70
    # cellularAutomataConfig = getUserConfig()
    cellularAutomataConfig = readCellularAutomataConfigFromFile("./config/stable.json")
    # Initialize Cellular Automaton and Game Window
    cellularAutomata = CellularAutomata(cellularAutomataConfig)
    game = GameWindow(cellularAutomataConfig.rows,
                      cellularAutomataConfig.columns, _cell_size, cellularAutomata)

    # Start the simulation
    game.start_game()

    # Extract statistics from the cellular automaton viewer
    average_temperatures = game.cellularAutomataViewer.stats.average_temperatures
    temperature_standard_deviation = game.cellularAutomataViewer.stats.temperature_standard_deviation
    min_temperatures = game.cellularAutomataViewer.stats.min_temperatures
    max_temperatures = game.cellularAutomataViewer.stats.max_temperatures

    # Calculate yearly averages
    average_pollutions = game.cellularAutomataViewer.stats.average_pollutions
    pollution_standard_deviation = game.cellularAutomataViewer.stats.pollution_standard_deviation
    min_pollutions = game.cellularAutomataViewer.stats.min_pollutions
    max_pollutions = game.cellularAutomataViewer.stats.max_pollutions

    runningAverageTemprature = 0
    runningTemperatureStandardDeviation = 0
    runningMinTemperature = 0
    runningMaxTemperature = 0

    runningAveragePollution = 0
    runningPollutionStandardDeviation = 0
    runningMinPollution = 0
    runningMaxPollution = 0

    for i in range(len(average_temperatures)):
        runningAverageTemprature += average_temperatures[i]
        runningTemperatureStandardDeviation += temperature_standard_deviation[i]
        runningMinTemperature += min_temperatures[i]
        runningMaxTemperature += max_temperatures[i]

        runningAveragePollution += average_pollutions[i]
        runningPollutionStandardDeviation += pollution_standard_deviation[i]
        runningMinPollution += min_pollutions[i]
        runningMaxPollution += max_pollutions[i]

    timeRunning = len(average_temperatures)
    yearlyAverageTemprature = runningAverageTemprature / timeRunning
    yearlyTemperatureStandardDeviation = runningTemperatureStandardDeviation / timeRunning
    yearlyMinTemperature = runningMinTemperature / timeRunning
    yearlyMaxTemperature = runningMaxTemperature / timeRunning
    yearlyAveragePollution = runningAveragePollution / timeRunning
    yearlyPollutionStandardDeviation = runningPollutionStandardDeviation / timeRunning
    yearlyMinPollution = runningMinPollution / timeRunning
    yearlyMaxPollution = runningMaxPollution / timeRunning

    # Create time axis
    time_axis = [i for i in range(len(average_temperatures))]
    # Normalize statistics
    average_temperatures = normalize_stats(average_temperatures,
                                           yearlyAverageTemprature)
    temperature_standard_deviation = normalize_stats(temperature_standard_deviation,
                                                     yearlyTemperatureStandardDeviation)
    min_temperatures = normalize_stats(min_temperatures,
                                       yearlyMinTemperature)
    max_temperatures = normalize_stats(max_temperatures,
                                       yearlyMaxTemperature)
    average_pollutions = normalize_stats(average_pollutions,
                                         yearlyAveragePollution)
    pollution_standard_deviation = normalize_stats(pollution_standard_deviation,
                                                   yearlyPollutionStandardDeviation)
    min_pollutions = normalize_stats(min_pollutions,
                                     yearlyMinPollution)
    max_pollutions = normalize_stats(max_pollutions,
                                     yearlyMaxPollution)
    # Show graphs
    plotMinMaxAverage(time_axis, min_temperatures, max_temperatures,
                      average_temperatures, "Temperature",
                      "Temperatures throughout time")
    plotMinMaxAverage(time_axis, min_pollutions, max_pollutions,
                      average_pollutions, "Pollution",
                      "Pollution throughout time")
    plot(time_axis, temperature_standard_deviation,
         "Temperature standard Deviation",
         "Temperature standard Deviation throughout time")
    plot(time_axis, pollution_standard_deviation,
         "Pollution standard Deviation",
         "Pollution standard Deviation throughout time")
