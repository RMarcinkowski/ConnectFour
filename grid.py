class Grid():
    def __init__(self):
        columns = 7
        rows = 6
        self.__grid = [0] * rows
        for i in range(rows):
            self.__grid[i] = [0] * columns

    def drop_disc(self, column):
        print("Disc dropped in column " + str(column))