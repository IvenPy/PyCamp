"""

"""
import unittest
from unittest import mock
from day_1 import matcher


class MyTestCase(unittest.TestCase):

    @mock.patch("main.matcher.os.path")
    @mock.patch("main.matcher.os")
    def test_invalid_path(self, mock_os, mock_path):
        mock_path.exists.return_value = True
        matcher.check_path_validation("some/path")

    def test_valid_path(self):
        pass

    def test_wrong_file_extension(self):
        pass


if __name__ == '__main__':
    unittest.main()
