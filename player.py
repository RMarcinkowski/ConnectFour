from enum import Enum

class Color(Enum):
    WHITE = 0
    BLUE = 1
    RED = 2
    GREEN = 3



class Intelligence(Enum):
    PLAYER = 0
    EASY = 1
    NORMAL = 2
    HARD = 3


class Player():

    def __init__(self, name, color, intelligence):
        """Create a player.

        :param name: name of the player
        :param color: color of the players disc
        :param intelligence: determine where it is a human(0) or an AI with 3 different levels
        """
        self.__name = name
        if isinstance(color, Color):
            self.__color = color
        if isinstance(intelligence, Intelligence):
            self.__intelligence = intelligence

    # properties
    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def intelligence(self):
        return self.__intelligence
