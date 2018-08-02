"""
"""
import copy


class Matrix:

    def __init__(self, matrix):
        self.__matrix = self.__set_matrix(matrix)
        self.__size = 0, 0
        self.__check_matrix()

    @property
    def size(self):
        return self.__size

    @property
    def matrix(self):
        return self.__matrix

    def __set_matrix(self, matrix):
        intern_matrix = []
        for row in matrix:
            intern_matrix.append(list(copy.deepcopy(row)))
        return intern_matrix

    def __check_matrix(self):
        """
        Checking created matrix on
        dimension. Fails if matrix is empty list or
        rows have different size.

        Returns: None

        """
        x, y = len(self.matrix), 0
        if x == 0:
            raise ValueError("You put 0 dimensional matrix")
        y = len(self.matrix[0])
        for ind, row in enumerate(self.matrix):
            if y != len(row):
                raise ValueError("Row №{} {} not in {} lenght"
                                 .format(ind, row, y))
        self.__size = (x, y)

    def check_instance(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Not supported operation:"
                            " + on Matrix and {}"
                            .format(type(other)))

        if self.size != other.size:
            raise ValueError("Matrix {} and {}"
                             " have different size"
                             .format(self.matrix, other.matrix))

    def __add__(self, other):
        """
        Addition of two matrix. Fails if
        matrices have different dimensions
        Args:
            other: matrix

        Returns: matrix: sum of two matrix

        """
        self.check_instance(other)
        matrix_sum = [[self.matrix[x][y] + other.matrix[x][y]
                       for y in range(self.size[1])]
                      for x in range(self.size[0])]
        return Matrix(matrix_sum)

    def T(self):
        return Matrix([list(i) for i in zip(*self.matrix)])

    def __radd__(self, other):
        return Matrix.__add__(self, other)

    def __iadd__(self, other):
        add_matrix = self.__add__(other)
        return add_matrix

    def __sub__(self, other):
        """
        Subtract of two matrixes. Fails if
        matrices have different dimensions
        Args:
            other: matrix

        Returns: matrix: sum of two matrix
        """
        self.check_instance(other)
        matrix_sum = [[self.matrix[x][y] - other.matrix[x][y]
                       for y in range(self.size[1])]
                      for x in range(self.size[0])]
        return Matrix(matrix_sum)

    @staticmethod
    def create_matrix(size, value):
        return Matrix([[value for row in range(size[1])]
                       for col in range(size[0])])

    def __mul__(self, other):
        """
        Multiplying of two matrices or matrix and int. Fails if
        matrices have different dimensions
        Args:
            other: matrix

        Returns: matrix: multiplying of two matrix

        """
        if type(other) is Matrix:
            if self.size[0] != other.size[1]:
                raise ValueError("Matrix {} and {} have different dimensions"
                                 .format(self, other))

            mult_matrix = Matrix.create_matrix((
                self.size[0], other.size[1]), 0) \
                .matrix

            for rows_s in range(self.__size[0]):
                for cols_o in range(other.size[1]):
                    for cols_s in range(self.__size[1]):
                        mult_matrix[rows_s][cols_o] += \
                            self.matrix[rows_s][cols_s] * other.matrix[cols_s][cols_o]

        elif type(other) is int:
            mult_matrix = [[self.matrix[x][y] * other
                            for y in range(self.size[1])]
                           for x in range(self.size[0])]

        else:
            raise TypeError("Unsupported operand * for Matrix and {}"
                            .format(type(other)))

        return Matrix(mult_matrix)

    def __imul__(self, other):
        mult_matrix = self.__mul__(other)
        return mult_matrix

    def __pow__(self, power, modulo=None):
        """
        Exponentiation matrix on itself power times
        Args:
            power:
            modulo:

        Returns:

        """
        if power == 0:
            return Matrix.create_matrix(self.size, 1)
        mult_matrix = self
        for x in range(power - 1):
            mult_matrix = self.__mul__(mult_matrix)
        return mult_matrix
