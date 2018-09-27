import pgzrun
import pygame as pg
from grid import *

rows = 6
columns = 7
g = Grid(rows,columns)

CELL_SIZE = 75
WIDTH = columns * CELL_SIZE + 20
HEIGHT = rows * CELL_SIZE + 200



def draw():
    screen.fill((200, 200, 200))
    grid = g.tolist()
    row_pos = 20
    for row in grid:
        column_pos = 10
        for cell in row:
            img = 'empty_field'
            if cell == 1:
                img = 'blue_field'
            elif cell == 2:
                img = 'red_field'

            cell_act = Actor(img)
            cell_act.topleft = column_pos, row_pos
            column_pos += CELL_SIZE
            cell_act.draw()
        row_pos += CELL_SIZE


def on_mouse_down(pos):
    xpos = pos[0]
    if 0 < xpos < CELL_SIZE * g.num_columns:
        pg.event.set_blocked(pg.MOUSEBUTTONDOWN)
        t = g.player_turn
        for i in range(0, g.num_columns + 1):
            if CELL_SIZE * i < xpos < CELL_SIZE * (i + 1):
                g.drop_disc(i)
                break
        clock.schedule_unique(allow_mouse, 0)
        draw()
        win_state = g.calc_if_won(t + 1)
        if win_state == "draw":
            end_match()
        elif win_state:
            end_match(t + 1)

def on_key_down(key):
    if key == pg.K_r:
        reset()


def allow_mouse():
    pg.event.set_allowed(pg.MOUSEBUTTONDOWN)


def end_match(num = None):

    end_text = "Unentschieden"
    if num != None:
        end_text = "Spieler " + str(num) + " hat gewonnen!"
    restart_text = "Drücke 'R', um neu zu starten."

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                done = True

        screen.draw.text(end_text, (20, HEIGHT - 170), fontsize=60, owidth=1.5,
                         ocolor=(255, 255, 255), color=(0, 0, 0), background=(200, 200, 200))
        screen.draw.text(restart_text, (20, HEIGHT - 100), fontsize=40, color=(0, 0, 0), background=(200, 200, 200))

        pg.display.flip()
    reset()


def reset():
    g.reset()

pg.init()
pgzrun.go()
