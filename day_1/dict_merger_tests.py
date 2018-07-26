import unittest
from day_1 import dict_merger


class MyTestCase(unittest.TestCase):
    def test_merge_without_intersection(self):
        d_1 = {1: 2, 2: 3}
        d_2 = {3: 4, 4: 5}
        d_3 = dict_merger.merge_dicts(d_1, d_2)
        self.assertDictEqual(d_3, {1: 2, 2: 3, 3:4, 4: 5})

    def test_merge_with_intersection(self):
        d_1 = {1: 2, 2: 3}
        d_2 = {1: 4, 2: 5}
        d_3 = dict_merger.merge_dicts(d_1, d_2)
        self.assertDictEqual(d_3, {1: 4, 2: 5})


if __name__ == '__main__':
    unittest.main()
