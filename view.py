from abc import ABC, abstractmethod

class View(ABC):
    def __init__(self, player1, player2):
        self._color_player1 = player1
        self._color_player2 = player2

    @abstractmethod
    def set_disc_position(self, name):
        raise NotImplementedError()

    @abstractmethod
    def show(self, grid):
        raise NotImplementedError()

class ConsoleView(View):
    def set_disc_position(self, name):
        position_set = False
        while not position_set:
            position = input(name + ", wähle eine Spalte von 0-6: ")
            try:
                position = int(position)
                if position < 0 or position > 6:
                    raise IndexError()
                return position
            except:
                print("Es muss eine Zahl von 0-6 sein!")

    def show(self, grid):
        print(" 0 1 2 3 4 5 6")
        for row in grid:
            rowString = " "
            for cell in row:
                if cell == 0:
                    rowString += "+ "
                elif cell == self._color_player1:
                    rowString += "0 "
                elif cell == self._color_player2:
                    rowString += "X "
            print(rowString)


class GUIView(View):
    def set_disc_position(self, name):
        raise NotImplementedError()

    def show(self, grid):
        raise NotImplementedError()
