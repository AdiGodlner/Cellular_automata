
from gameWindow import GameWindow

if __name__ == '__main__':
    #  TODO remember in documentation and read me there is a need to install tkinter
    # and or make into an exe

    _width, _height = 10, 10
    _cell_size = 70

    game = GameWindow(_width, _height, _cell_size)
    game.start_game()
    # window.mainloop() # what is that and what does it do

    # canvas = tk.Canvas(window, bg="black")
    # canvas.pack()
    # canvas.create_rectangle((50,20,10,10),fill="red")
