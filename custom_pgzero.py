import pgzrun
import pygame as pg
import time
from grid import *
from view import *
from player import *

WIDTH = 800
HEIGHT = 800
CELL_SIZE = 75
TURN_COUNT = -1

pg.init()

class PgzView(View):

    def set_disc_position(self, name):
        raise NotImplementedError()

    def show(self, grid):
        row_pos = 0
        for row in grid:
            column_pos = 0
            for cell in row:
                img = 'empty_field'
                if cell == self._color_player1.value:
                    img = 'blue_field'
                elif cell == self._color_player2.value:
                    img = 'red_field'

                cell_act = Actor(img)
                cell_act.topleft = column_pos, row_pos
                column_pos += CELL_SIZE
                cell_act.draw()
            row_pos += CELL_SIZE

    def win(self, num):
        text = "Spieler " + str(num) + " hat gewonnen!"
        font = pg.font.SysFont('Comic Sans MS', 20)
        text = font.render(text, 1, (0,0,0))
        screen.blit(text, (100, 500))
        pg.display.flip()
        time.sleep(3)

    def update(self):
        grid = g.tolist()
        view.show(grid)
        for i in range(1,3):
            if g.calc_if_won(i):
                win(i)


def draw():
    screen.fill((200, 200, 200))
    grid = g.tolist()
    view.show(grid)

def on_mouse_down(pos):
    if 0 < pos[0] < CELL_SIZE * 7:
        pg.event.set_blocked(pg.MOUSEBUTTONDOWN)
        t = player_turn()
        if 0 < pos[0] < CELL_SIZE:
            g.drop_disc(0, t)
        elif CELL_SIZE < pos[0] < CELL_SIZE * 2:
            g.drop_disc(1, t)
        elif CELL_SIZE * 2 < pos[0] < CELL_SIZE * 3:
            g.drop_disc(2, t)
        elif CELL_SIZE * 3 < pos[0] < CELL_SIZE * 4:
            g.drop_disc(3, t)
        elif CELL_SIZE * 4 < pos[0] < CELL_SIZE * 5:
            g.drop_disc(4, t)
        elif CELL_SIZE * 5 < pos[0] < CELL_SIZE * 6:
            g.drop_disc(5, t)
        elif CELL_SIZE * 6 < pos[0] < CELL_SIZE * 7:
            g.drop_disc(6, t)

        clock.schedule_unique(allow_mouse, 0.5)


def allow_mouse():
    pg.event.set_allowed(pg.MOUSEBUTTONDOWN)


def player_turn():
    global TURN_COUNT
    TURN_COUNT += 1
    return (TURN_COUNT % 2) + 1


def update():
    view.update()

def win(num):
    view.win(num)
    reset()

def reset():
    global TURN_COUNT
    TURN_COUNT = -1
    g.reset()


g = Grid()
view = PgzView(Color.BLUE, Color.RED)


pgzrun.go()
