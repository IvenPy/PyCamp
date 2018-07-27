import unittest
from day_1 import dict_merger
from unittest import mock


class MyTestCase(unittest.TestCase):

    @mock.patch("builtins.print", autospec=True, side_effects=True)
    def test_merge_without_intersection(self, mock_output):
        d_1 = {1: 2, 2: 3}
        d_2 = {3: 4, 4: 5}
        d_3 = dict_merger.merge_dicts(d_1, d_2)
        self.assertDictEqual(d_3, {1: 2, 2: 3, 3: 4, 4: 5})
        mock_output.assert_called_with("Keys updated successfully, no intersection")

    @mock.patch("builtins.print", autospec=True, side_effects=True)
    def test_merge_with_intersection(self, mock_output):
        d_1 = {1: 2, 2: 3}
        d_2 = {3: 4, 2: 5}
        d_3 = dict_merger.merge_dicts(d_1, d_2)
        self.assertDictEqual(d_3, {1: 2, 3: 4, 2: 5})
        mock_output.assert_called_with("Key 2 updated from - 3 to - 5")


if __name__ == '__main__':
    unittest.main()
