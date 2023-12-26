from gameWindow import GameWindow
import json
from configs import CellularAutomataConfig
from cellularAutomata import CellularAutomata


def getCellularAutomataConfigFromFile(fileName):
    with open(fileName, 'r') as f:
        config = json.load(f)
    return CellularAutomataConfig(**config)


if __name__ == '__main__':
    #  TODO remember in documentation and read me there is a need to install tkinter
    # and or make into an exe

    _cell_size = 70
    cellularAutomataConfig = getCellularAutomataConfigFromFile("./config/test.json")
    cellularAutomata = CellularAutomata(cellularAutomataConfig)
    game = GameWindow(cellularAutomataConfig.rows,
                      cellularAutomataConfig.columns, _cell_size, cellularAutomata)
    game.start_game()
    # window.mainloop() # what is that and what does it do

    # canvas = tk.Canvas(window, bg="black")
    # canvas.pack()
    # canvas.create_rectangle((50,20,10,10),fill="red")
