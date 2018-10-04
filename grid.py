import numpy as np

class Grid():
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__grid = np.zeros(shape=(self.__rows, self.__columns), dtype=int)
        self.__player_turn = 0
        self.__turn_count = 0

    @property
    def player_turn(self):
        return self.__player_turn

    @property
    def num_rows(self):
        return self.__rows

    @property
    def num_columns(self):
        return self.__columns


    def tolist(self):
        return self.__grid.tolist()


    def reset(self):
        self.__turn_count = 0
        self.__player_turn = 0
        self.__grid = np.zeros(shape=(self.__rows, self.__columns), dtype=int)


    def drop_disc(self, column, num = None):
        if num is None:
            num = self.player_turn + 1
        current_column = self.__grid[:, column]
        result_column = current_column
        drop_possible = False
        for i in range(self.__rows):
            if result_column[-(i+1)] == 0:
                result_column[-(i+1)] = num
                drop_possible = True
                break
        if not drop_possible:
            return False
        self.__grid[:, column] = result_column
        self.__turn_count += 1
        self.__player_turn = (self.__player_turn + 1) % 2
        return True


    def calc_if_won(self, num):
        if self.__check_rows(self.__grid, num) or self.__check_columns(self.__grid.transpose(), num) or self.__check_diagonal(num):
            return True
        if self.__turn_count == self.num_columns * self.num_rows:
            return "draw"
        return False

    def __row_wins(self, row, num):
        num_count = 0
        for cell in row:
            if cell == num:
                num_count += 1
            else:
                num_count = 0
            if num_count == 4:
             return True
        return False


    def __check_rows(self, rows, num):
        for row in rows:
            if self.__row_wins(row, num):
                return True
        return False


    def __check_columns(self, columns, num):
        for column in columns:
            if self.__row_wins(column, num):
                return True
        return False


    def __check_diagonal(self, num):
        for i in range(self.__columns-3):
            if self.__row_wins(self.__grid.diagonal(i), num):
                return True
            if self.__row_wins(self.__grid[:, ::-1].diagonal(i), num):
                return True

        for i in range(1,self.__rows-3):
            if self.__row_wins(self.__grid.diagonal(i), num):
                return True
            if self.__row_wins(self.__grid[:, ::-1].diagonal(-i), num):
                return True
        return False
