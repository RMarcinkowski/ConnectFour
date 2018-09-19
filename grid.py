import numpy as np

class Grid():
    def __init__(self):
        self.__columns = 7
        self.__rows = 6
        self.__grid = np.zeros(shape=(self.__rows, self.__columns), dtype=int)


    def tolist(self):
        return self.__grid.tolist()


    def drop_disc(self, column, num):
        current_column = self.__grid[:, column]
        result_column = current_column
        drop_possible = False
        for i in range(self.__rows):
            if result_column[-(i+1)] == 0:
                result_column[-(i+1)] = num
                drop_possible = True
                break
        if not drop_possible:
            raise IndexError("This column is already full")
        self.__grid[:, column] = result_column


    def calc_if_won(self, num):
        return self.__check_rows(self.__grid, num) or self.__check_columns(self.__grid.transpose(), num) or self.__check_diagonal(num)


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
