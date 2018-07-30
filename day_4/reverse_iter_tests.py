import unittest
from day_4.reverse_iter import reverse_iter


class MyTestCase(unittest.TestCase):
    def test_reverse_iteration(self):
        l = [1, 2, 3, 4]
        reverse_l = list(reverse_iter(l))
        self.assertEqual(reverse_l, [4, 3, 2, 1])
        t = (1, 2, 3, 4)
        reverse_t = tuple(reverse_iter(t))
        self.assertEqual(reverse_t, (4, 3, 2, 1))


if __name__ == '__main__':
    unittest.main()
