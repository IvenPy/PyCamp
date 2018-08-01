"""



"""
class Matrix:

    def __init__(self, rows):
        self.matrix = rows
        self.size = 0, 0
        self.check_matrix()

    def check_matrix(self):
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
        self.size = (x, y)

    def __add__(self, other):
        """
        Addition of two matrix. Fails if
        matrixes have different dimensions
        Args:
            other: matrix

        Returns: matrix: sum of two matrix

        """
        if not isinstance(other, Matrix):
            raise TypeError("Not supported operation:"
                            " add on Matrix and {}"
                            .format(type(other)))

        if self.size != other.size:
            raise ValueError("Matrix {} and {}"
                             " have different size"
                             .format(self.matrix, other.matrix))

        matrix_sum = []
        for x in range(0, self.size[0]):
            matrix_sum.append([])
            for y in range(0, self.size[1]):
                matrix_sum[x].append(self.matrix[x][y] + other.matrix[x][y])
        return Matrix(matrix_sum)

    def T(self):
        pass

    def __radd__(self, other):
        return Matrix.__add__(self, other)

    def __iadd__(self, other):
        add_matrix = self.__add__(other)
        return add_matrix

    def __sub__(self, other):
        """
        Subtract of two matrixes. Fails if
        matrixes have different dimensions
        Args:
            other: matrix

        Returns: matrix: sum of two matrix

        """
        if not isinstance(other, Matrix):
            raise TypeError("Not supported operation:"
                            " add on Matrix and {}"
                            .format(type(other)))

        if self.size != other.size:
            raise ValueError("Matrix {} and {}"
                             " have different size"
                             .format(self.matrix, other.matrix))

        matrix_sum = []
        for x in range(0, self.size[0]):
            matrix_sum.append([])
            for y in range(0, self.size[1]):
                matrix_sum[x].append(self.matrix[x][y] - other.matrix[x][y])
        return Matrix(matrix_sum)

    def __mul__(self, other):
        if type(other) is Matrix:
            if self.size != tuple(reversed(other.size)):
                raise ValueError("Matrix {} and {} have different dimensions"
                                 .format(self, other))

            mult_matrix = [[0 for row in range(self.size[0])]
                           for col in range(self.size[0])]

            for rows_s in range(self.size[0]):
                for cols_o in range(other.size[1]):
                    for cols_s in range(self.size[1]):
                        mult_matrix[rows_s][cols_o] += \
                            self.matrix[rows_s][cols_s] * other.matrix[cols_s][cols_o]

        elif type(other) is int:
            mult_matrix = []

            for x in range(0, self.size[0]):
                mult_matrix.append([])
                for y in range(0, self.size[1]):
                    mult_matrix[x].append(self.matrix[x][y] * other)
        else:
            raise ValueError()

        return Matrix(mult_matrix)

    def __imul__(self, other):
        mult_matrix = self.__mul__(other)
        return mult_matrix

    def __pow__(self, power, modulo=None):
        for x in range(power - 1):
            mult_matrix = self.__mul__(self)
        return mult_matrix