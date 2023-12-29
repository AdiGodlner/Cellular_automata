import math
import matplotlib.pyplot as plt


def normalize_stats(stats, average):
    """
     Normalize a list of statistics based on its average and standard deviation

     :param stats: (list) The list of statistics to normalize
     :param average: (float) The average value of the statistics
     :return: (list) The normalized data
     """
    standard_deviation = calculate_standard_deviation(stats, average)
    normalized_data = [(x - average) / standard_deviation for x in stats]
    return normalized_data


def plotMinMaxAverage(x_values, minData, maxData, averageData, label, title):
    """
    Plot the minimum, maximum, and average values over time.

    :param x_values: (list) The x-axis values (time)
    :param minData: (list) The minimum values over time
    :param maxData: (list) The maximum values over time
    :param averageData: (list) The average values over time
    :param label: (str) The label for the y-axis
    :param title: (str) The title of the plot
    """

    # Sample data
    # Plotting the data
    plt.plot(x_values, minData, label=f"min {label}")
    plt.plot(x_values, maxData, label=f"max {label}")
    plt.plot(x_values, averageData, label=f"average {label}")

    # Adding labels and title
    plt.xlabel("time")
    plt.ylabel(label)
    plt.title(title)

    # Adding a legend
    plt.legend()
    # Display the graph
    plt.show()


def plot(x_values, y_values, label, title):
    """
    Plot a set of values over time

    :param x_values: (list) The x-axis values (time)
    :param y_values: (list) The y-axis values
    :param label: (str) The label for the y-axis
    :param title: (str) The title of the plot
    """
    # Adding labels and title
    plt.plot(x_values, y_values, label=label)
    plt.xlabel("time")
    plt.ylabel(label)
    plt.title(title)

    # Adding a legend
    plt.legend()
    # Display the graph
    plt.show()


def calculate_standard_deviation(stats, average):
    """
    Calculate the standard deviation of a set of statistics

    :param stats: (list) The list of statistics
    :param average: (float) The average value of the statistics
    :return: (float) The standard deviation
    """
    # calculate the standard deviation (square root of variance)
    variance = calculate_variance(stats, average)
    return math.sqrt(variance)


def calculate_variance(stats, average):
    """
    Calculate the variance of a set of statistics

    :param stats: (list) The list of statistics
    :param average: (float) The average value of the statistics
    :return: (float) The variance
    """
    # calculate the variance (average squared difference)
    squared_diff_sum = sum((measurement - average) ** 2 for measurement in stats)
    return squared_diff_sum / len(stats)


class Stats:
    """
    A container for storing statistics related to the cellular automata simulation
    """

    def __init__(self):
        self.temperature_standard_deviation = []
        self.average_temperatures = []
        self.min_temperatures = []
        self.max_temperatures = []

        self.pollution_standard_deviation = []
        self.average_pollutions = []
        self.min_pollutions = []
        self.max_pollutions = []
