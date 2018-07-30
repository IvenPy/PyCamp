import unittest
from day_4.yarange import Yarange


class MyTestCase(unittest.TestCase):
    def test_(self):
        g = iter(Yarange(0, 3))
        res = []
        for x in range(0, 9):
            res.append(next(g))
        self.assertEqual(res, [0, 1, 2, 0, 1, 2, 0, 1, 2])


if __name__ == '__main__':
    unittest.main()
