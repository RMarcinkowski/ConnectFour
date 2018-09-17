from player import *
from grid import *
from view import *

def player_won():
    return False

run_program = True
while run_program:

    grid = Grid()
    name1 = input("Gib den Namen von Spieler 1 ein: ")
    color1 = Color.BLUE
    player1 = Player(name1, color1, Intelligence.PLAYER)

    name2 = input("Gib den Namen von Spieler 2 ein: ")
    color2 = Color.RED

    # todo: Mensch oder AI
    intelligence = Intelligence.PLAYER

    player2 = Player(name2, color2, intelligence)
    player_array = [player1, player2]

    run_game = True
    while run_game:
        for p in player_array:
            position = set_disc_position()
            grid.drop_disc(position)
            # todo: show Konsole oder GUI
            if (player_won()):
                run_game = False
                break

    print("Vorbei")




