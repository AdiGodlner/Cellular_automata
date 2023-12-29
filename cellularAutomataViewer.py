from cellularAutomataStatsViewer import *
from cellularAutomataBoardViewer import *
from stats import Stats, calculate_standard_deviation


class CellularAutomataViewer(ttk.Frame):
    """
    The GUI for the cellular automata simulation
     displaying both statistics and the board.

    Attributes:
        year (int): The current year in the simulation
        cellularAutomata (CellularAutomata): The cellular automata instance for simulation
        columns (int): The number of columns in the cellular automata grid
        rows (int): The number of rows in the cellular automata grid
        stats (Stats): The statistics object for tracking simulation data
        statsViewer (CellularAutomataStatsViewer): The GUI for displaying simulation statistics
        cellularAutomataBoardViewer (CellularAutomataBoardViewer): The GUI for displaying the cellular automata board
    """
    def __init__(self, parent, cellularAutomata, columns, rows, cell_size):
        super().__init__(parent)
        self.year = 0
        self.cellularAutomata = cellularAutomata
        self.columns = columns
        self.rows = rows
        self.stats = Stats()
        self.statsViewer = CellularAutomataStatsViewer(self, self.stats)
        self.cellularAutomataBoardViewer = CellularAutomataBoardViewer(self, cellularAutomata,
                                                                       columns, rows, cell_size)
        self.create_layout()
        # Create a vertical scrollbar

    def create_layout(self):
        """
        Creates the window layout
        """
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.statsViewer.grid(row=0, column=0, sticky='nsew')
        self.cellularAutomataBoardViewer.grid(row=0, column=1, sticky='nsew')

    def draw_board(self):
        """
        Draws the current state of the cellular automata board
        updates statistics and displays them
        """
        board = self.cellularAutomata.get_active_board()
        runningTemprature = 0
        runningPollution = 0

        minTemprature = board[0][0].config.temperature
        maxTemprature = board[0][0].config.temperature

        minPollution = board[0][0].config.wind.pollution
        maxPollution = board[0][0].config.wind.pollution

        temperatures = []
        pollutions = []

        for i in range(self.rows):
            for j in range(self.columns):
                currCell = board[i][j]
                self.cellularAutomataBoardViewer.draw_cell(i, j, currCell.get_text(), currCell.config.color)

                currTemprature = currCell.config.temperature
                temperatures.append(currTemprature)

                if currTemprature < minTemprature:
                    minTemprature = currTemprature
                elif currTemprature > maxTemprature:
                    maxTemprature = currTemprature

                currPollution = currCell.config.wind.pollution
                pollutions.append(currPollution)

                if currPollution < minPollution:
                    minPollution = currPollution
                elif currPollution > maxPollution:
                    maxPollution = currPollution

                runningTemprature += currTemprature
                runningPollution += currPollution

        # redraw stats
        averageTemprature = runningTemprature / (self.rows * self.columns)
        tempratureStandardDeviation = calculate_standard_deviation(temperatures, averageTemprature)

        self.statsViewer.updateStatByName(AVERAGE_TEMPERATURE, averageTemprature)
        self.statsViewer.updateStatByName(TEMPRATURE_STANDARD_DEVIATION, tempratureStandardDeviation)
        self.statsViewer.updateStatByName(MIN_TEMPRATURE, minTemprature)
        self.statsViewer.updateStatByName(MAX_TEMPRATURE, maxTemprature)

        averagePollution = runningPollution / (self.rows * self.columns)
        pollutionStandardDeviation = calculate_standard_deviation(pollutions, averagePollution)

        self.statsViewer.updateStatByName(AVERAGE_POLLUTION, averagePollution)
        self.statsViewer.updateStatByName(POLLUTION_STANDARD_DEVIATION, pollutionStandardDeviation)
        self.statsViewer.updateStatByName(MIN_POLLUTION, minPollution)
        self.statsViewer.updateStatByName(MAX_POLLUTION, maxPollution)

        self.statsViewer.updateStatByName(SEASON, board[0][0].getSeason())
        self.statsViewer.updateStatByName(RUNTIME, f"year: {self.year} | day {board[0][0].config.time}")

        if board[0][0].config.time == 0:
            self.year += 1
