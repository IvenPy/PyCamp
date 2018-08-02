import unittest
from day_5.matrix import Matrix


class MyTestCase(unittest.TestCase):
    def test_adding_two_equal_matrix(self):
        m1 = Matrix([[1], [2], [3]])
        m2 = Matrix([[1], [2], [3]])
        m3 = m1 + m2
        self.assertEqual(m3.matrix, [[2], [4], [6]])

    def test_multiplying_matrix_on_number(self):
        m1 = Matrix([[1], [2], [3]]) * 3
        self.assertEqual(m1.matrix, [[3], [6], [9]])

    def test_fall_on_different_dimensions_matrices(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[1], [2], [3]])
        with self.assertRaises(ValueError) as e:
            m3 = m1 + m2

        with self.assertRaises(ValueError) as e:
            m3 = m1 * m2

        with self.assertRaises(ValueError) as e:
            m3 = m1 - m2

    def test_creating_zero_matrix(self):
        self.assertEqual(Matrix.create_matrix((2, 3), value=0).matrix,
                         [[0, 0, 0], [0, 0, 0]])

    def test_multiplying_matrix_on_matrix(self):
        m1 = Matrix([[1, 2, 3]])
        m2 = Matrix([[1], [2], [3]])
        m3 = m1 * m2
        self.assertEqual(m3.matrix, [[14]])
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        m2 = Matrix([[1, 2, 3], [4, 5, 6]])
        m3 = m1 * m2
        self.assertEqual([[9, 12, 15], [19, 26, 33], [29, 40, 51]], m3.matrix)

    def test_inplace_add(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[7, 8, 9], [10, 11, 12]])
        m1 += m2
        self.assertEqual(m1.matrix, [[8, 10, 12], [14, 16, 18]])

    def test_subtraction(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[4, 5], [6, 7]])
        m3 = m2 - m1
        self.assertEqual(m3.matrix, [[3, 3], [3, 3]])

    def test_pow(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = m1 ** 2
        self.assertEqual(m2.matrix, [[7, 10], [15, 22]])
        m3 = m1 ** 3
        self.assertEqual(m3.matrix, [[37, 54], [81, 118]])

    def test_transposition(self):
        m1 = Matrix([[1, 2], [3, 4], [5, 6]])
        m2 = m1.T()
        self.assertEqual(m2.matrix, [[1, 3, 5], [2, 4, 6]])


if __name__ == '__main__':
    unittest.main()
