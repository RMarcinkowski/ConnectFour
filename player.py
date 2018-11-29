from enum import Enum
from medium_ai import *
import random

class Color(Enum):
    WHITE = 0
    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4



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


    def AI_set_drop(self, grid):
        if self.intelligence == Intelligence.EASY:
            return self.__AI_easy_drop(grid)
        elif self.intelligence == Intelligence.NORMAL:
            return self.__AI_normal_drop(grid)
        else:
            return self.__AI_hard_drop(grid)


    def __AI_easy_drop(self, grid):
        x = random.randrange(len(grid.tolist()))
        return x

    def __AI_normal_drop(self, grid):
        b = Board()
        b.convert(grid.get_grid(), self.color.value)
        move = b.best()
        return move


    def __AI_hard_drop(self, grid):
        raise NotImplementedError()
