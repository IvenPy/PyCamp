"""

"""
import unittest
from unittest import mock
from day_1 import matcher


def test_path_validation_template(mock_path,
                                  exists, isfile, path):
    mock_path.exists.return_value = exists
    mock_path.isfile.return_value = isfile
    matcher.check_path_validation(path)


class MyTestCase(unittest.TestCase):

    @mock.patch("day_1.matcher.os.path")
    @mock.patch("day_1.matcher.os")
    def test_invalid_path(self, mock_os, mock_path):
        path = "some/invalid/path"
        with self.assertRaises(OSError):
            test_path_validation_template(mock_path, exists=False,
                                          isfile=False, path=path)

    @mock.patch("day_1.matcher.os.path")
    @mock.patch("day_1.matcher.os")
    def test_not_file(self, mock_os, mock_path):
        path = "some/path/to/dir"
        with self.assertRaises(OSError):
            test_path_validation_template(mock_path, exists=True,
                                          isfile=False, path=path)

    @mock.patch("day_1.matcher.os.path")
    @mock.patch("day_1.matcher.os")
    def test_wrong_file_extension(self, mock_os, mock_path):
        path = "some/path/without_csv_extension"
        with self.assertRaises(OSError):
            test_path_validation_template(mock_path, exists=True,
                                          isfile=True, path=path)

    @mock.patch("day_1.matcher.os.path")
    @mock.patch("day_1.matcher.os")
    def test_file_not_specified(self, mock_os, mock_path):
        path = None
        with self.assertRaises(OSError):
            test_path_validation_template(mock_path, exists=False,
                                          isfile=False, path=path)

    @mock.patch("day_1.matcher.os.path")
    @mock.patch("day_1.matcher.os")
    def test_valid_path(self, mock_os, mock_path):
        path = "good/path/to/file.csv"
        self.assertIsNone(test_path_validation_template(
            mock_path, exists=True, isfile=True, path=path))

    def test_calculating_matches(self):
        data = [
            {
                'name': 'ivan',
                'id': '1',
                'job': 'artist'
            },
            {
                'name': 'sarah',
                'id': '2',
                'job': 'artist'
            },
            {
                'name': 'ivan',
                'id': '3',
                'job': 'programmer'
            }]
        dict_matches = matcher.calculate_matches(data)
        assert_dict = [{'count': 2, 'key': 'name', 'value': 'ivan'},
                       {'count': 1, 'key': 'id', 'value': '1'},
                       {'count': 2, 'key': 'job', 'value': 'artist'},
                       {'count': 1, 'key': 'name', 'value': 'sarah'},
                       {'count': 1, 'key': 'id', 'value': '2'},
                       {'count': 1, 'key': 'id', 'value': '3'},
                       {'count': 1, 'key': 'job', 'value': 'programmer'}]

        self.assertEqual(dict_matches, assert_dict)


if __name__ == '__main__':
    unittest.main()
