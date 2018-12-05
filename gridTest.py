import unittest
from grid import *

class drop_disc_test(unittest.TestCase):
    def testcase_00(self):
        g = Grid(6,7)
        grid = g.tolist()
        for row in grid:
            for cell in row:
                self.assertEqual(0, cell)

        g.drop_disc(2, 2)
        grid = g.tolist()
        print(grid)
        self.assertEqual(2, grid[5][2])

        g.drop_disc(2, 1)
        grid = g.tolist()
        self.assertEqual(1, grid[4][2])

        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        self.assertFalse(g.drop_disc(2,1))

class calc_if_won_test(unittest.TestCase):
    def testcase_00(self):
        g = Grid(6,7)
        g.drop_disc(0, 1) # column: 0, color: 1
        g.drop_disc(1, 1)
        g.drop_disc(1, 1)
        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        self.assertFalse(g.calc_if_won(1))
        g.drop_disc(3, 2)
        g.drop_disc(3, 2)
        g.drop_disc(3, 2)
        self.assertFalse(g.calc_if_won(2))
        g.drop_disc(3, 1)
        self.assertTrue(g.calc_if_won(1)) # diagonal win

    def testcase_01(self):
        g = Grid(6,7)
        g.drop_disc(3, 1) # column: 0, color: 1
        g.drop_disc(2, 2)
        g.drop_disc(2, 1)
        g.drop_disc(1, 2)
        g.drop_disc(1, 1)
        g.drop_disc(0, 2)
        g.drop_disc(1, 1)
        g.drop_disc(0, 2)
        g.drop_disc(0, 1)
        g.drop_disc(3, 2)
        g.drop_disc(0, 1)
        self.assertTrue(g.calc_if_won(1)) # diagonal win

    def testcase_02(self):
        g = Grid(6,7)

        for j in range(6):
            for i in range(7):
                wert = j*7+i+1
                g.drop_disc(i,wert)

        grid = g.get_grid()
        print(grid)

        print("columns")
        for i in range(7-3):
            print(grid.diagonal(-i))
            print(grid[:, ::-1].diagonal(i))

        print("rows")
        for i in range(1,6-3):
            print(grid.diagonal(i))
            print(grid[:, ::-1].diagonal(-i))


if __name__ == "__main__":
    unittest.main()