import unittest
from day_4.single_generator import Integers


class MyTestCase(unittest.TestCase):
    def test_singleton(self):
        res = []
        i1 = Integers()
        for x in range(5):
            res.append(next(i1))
        i2 = Integers()
        for x in range(6, 10):
            res.append(next(i2))
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
