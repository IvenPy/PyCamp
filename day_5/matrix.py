class Matrix:
    def __init__(self, rows):
        self.matrix = rows
        self.size = 0, 0
        self.check_matrix()

    def check_matrix(self):
        x, y = len(self.matrix), 0
        if x == 0:
            raise ValueError("You put 0 dimensional matrix")
        y = len(self.matrix[0])
        for i, row in enumerate(self.matrix):
            if y != len(row):
                break
        # else:
        #     raise ValueError("Row №{} {} not in {} lenght"
        #                      .format(x, row, y))
        self.size = (x, y)

    def T(self):
        pass

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Not supported operation:"
                            " add on Matrix and {}"
                            .format(type(other)))
        if self.size != other.size:
            raise ValueError("Matrix {} and {}"
                             " have different size"
                             .format(self.matrix, other.matrix))
        matrix_sum = [a]
        print(self.size)
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                matrix_sum[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return matrix_sum
    
    def __radd__(self, other):
        return Matrix.__add__(self, other)


    def __iadd__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __imul__(self, other):
        pass
