from tkinter import ttk

RUNTIME = "runTime"
SEASON = "season"

AVERAGE_TEMPERATURE = "average_temperature"
TEMPRATURE_STANDARD_DEVIATION = "temprature_standard_deviation"
MIN_TEMPRATURE = "min_temprature"
MAX_TEMPRATURE = "max_temprature"

AVERAGE_POLLUTION = "average_pollution"
POLLUTION_STANDARD_DEVIATION = "pollution_standard_deviation"
MIN_POLLUTION = "min_pollution"
MAX_POLLUTION = "max_pollution"


class CellularAutomataStatsViewer(ttk.Frame):

    def __init__(self, parent, stats):
        """
        GUI for displaying statistics related to the cellular automata simulation
        """
        super().__init__(parent)
        self.stats = stats
        self.runTime = self.makeLabel("year : N/A")
        self.season = self.makeLabel("season : N/A")

        self.average_temperature = self.makeLabel("Average Temperature: N/A")
        self.temperature_standard_deviation = self.makeLabel("Temperature standard deviation : N/A")
        self.min_temprature = self.makeLabel("Min Temperature: N/A")
        self.max_temprature = self.makeLabel("Max Temperature: N/A: N/A")

        self.average_pollution = self.makeLabel("Average Pollution: N/A")
        self.pollution_standard_deviation = self.makeLabel("Pollution standard deviation : N/A")
        self.min_pollution = self.makeLabel("Min Pollution: N/A: N/A")
        self.max_pollution = self.makeLabel("Max Pollution: N/A: N/A")

    def makeLabel(self, text):
        """
        Creates and returns a ttk.Label with specified text

        :param text: The text to display on the label
        :return: The created ttk.Label
        """
        label = ttk.Label(self, text=text, padding=5, font=("Arial", 12, "bold"))
        label.pack()
        return label

    def updateStatByName(self, statName, stat):
        """
        Updates the displayed statistics based on the statistics name

        :param statName: The name of the statistic to update
        :param stat: The new value of the statistic
        """
        if statName == RUNTIME:
            self.runTime.config(text=stat)

        elif statName == SEASON:
            self.season.config(text=f"season: {stat}")

        elif statName == AVERAGE_TEMPERATURE:
            self.average_temperature.config(text=f"Average Temprature: {stat:2f}")
            self.stats.average_temperatures.append(stat)

        elif statName == TEMPRATURE_STANDARD_DEVIATION:
            self.temperature_standard_deviation.config(text=f"Temperature standard deviation:{stat:2f}")
            self.stats.temperature_standard_deviation.append(stat)

        elif statName == MIN_TEMPRATURE:
            self.min_temprature.config(text=f"Min Temperature:{stat}")
            self.stats.min_temperatures.append(stat)

        elif statName == MAX_TEMPRATURE:
            self.max_temprature.config(text=f"Max Temperature:{stat}")
            self.stats.max_temperatures.append(stat)

        elif statName == AVERAGE_POLLUTION:
            self.average_pollution.config(text=f"Average Pollution: {stat:2f}")
            self.stats.average_pollutions.append(stat)

        elif statName == POLLUTION_STANDARD_DEVIATION:
            self.pollution_standard_deviation.config(text=f"Pollution standard deviation:{stat:2f}")
            self.stats.pollution_standard_deviation.append(stat)

        elif statName == MIN_POLLUTION:
            self.min_pollution.config(text=f"Min Pollution:{stat:2f}")
            self.stats.min_pollutions.append(stat)

        elif statName == MAX_POLLUTION:
            self.max_pollution.config(text=f"Max Pollution:{stat:2f}")
            self.stats.max_pollutions.append(stat)
