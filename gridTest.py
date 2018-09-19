import unittest
from grid import *

class drop_disc_test(unittest.TestCase):
    def testcase_00(self):
        g = Grid()
        grid = g.tolist()
        for row in grid:
            for cell in row:
                self.assertEqual(0, cell)

        g.drop_disc(2, 2)
        grid = g.tolist()
        self.assertEqual(2, grid[5][2])

        g.drop_disc(2, 1)
        grid = g.tolist()
        self.assertEqual(1, grid[4][2])

        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        g.drop_disc(2, 1)
        self.assertRaises(IndexError, g.drop_disc, 2, 1)

class calc_if_won_test(unittest.TestCase):
    def testcase_00(self):
        g = Grid()
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

if __name__ == "__main__":
    unittest.main()