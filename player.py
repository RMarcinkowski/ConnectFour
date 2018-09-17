from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


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

    # getter
    def __get_name(self):
        return self.__name

    def __get_color(self):
        return self.__color

    def __get_intelligence(self):
        return self.__intelligence

    # properties
    Name = property(__get_name, None)
    Color = property(__get_color, None)
    Intelligence = property(__get_intelligence, None)