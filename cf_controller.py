from player import *
from grid import *
from view import *

class CF_Controller():
    def __init__(self):
        self.main_loop()

    def main_loop(self):
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

            view = ConsoleView(player1.color.value, player2.color.value)
            view.show(grid.tolist())
            run_game = True
            while run_game:
                for p in player_array:
                    position = view.set_disc_position(p.name)
                    grid.drop_disc(position, p.color.value)
                    view.show(grid.tolist())
                    if grid.calc_if_won(p.color.value):
                        run_game = False
                        print(p.name + " hat gewonnen!")
                        break

            print("Vorbei")

if __name__ == "__main__":
    CF_Controller()

