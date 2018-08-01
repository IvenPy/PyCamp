import unittest
from day_5.matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_creating(self):
        m = Matrix([[1], [2], [3]])
        m2 = Matrix([[1], [2], [3]])
        m3 = m + m2
        print(m3)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
