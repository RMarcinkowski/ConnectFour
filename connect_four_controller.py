from player import *
from grid import *
from view import *

class CF_Controller():
    def __init__(self):
        self.main_loop()

    def main_loop(self):
        grid = Grid(6, 7)
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

        run_program = True
        while run_program:
            grid.reset()
            view.show(grid.tolist())
            run_game = True
            while run_game:
                for p in player_array:
                    dropped = False
                    while not dropped:
                        position = view.set_disc_position(p.name)
                        dropped = grid.drop_disc(position, p.color.value)
                        if not dropped:
                            print("Spalte ist schon voll!")

                    view.show(grid.tolist())
                    win_state = grid.calc_if_won(p.color.value)
                    if win_state == "draw":
                        run_game = False
                        print("Unentschieden!")
                        break
                    elif win_state:
                        run_game = False
                        print(p.name + " hat gewonnen!")
                        break

            # ask for repetition
            repeat = input("\n\nErneut spielen? 'j' eingeben")
            if repeat != "j":
                run_program = False


if __name__ == "__main__":
    CF_Controller()

