class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for i in range(cols)] for j in range(rows)]

    def plus(self, matrix):
        if self.cols != matrix.cols or self.rows != matrix.rows:
            return "Матрицы разного размера"
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += matrix.data[i][j]

    def minus(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            return "Матрицы разного размера"
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] -= matrix.data[i][j]

    def multiply(self, matrix):
        if self.cols != matrix.rows:
            return "Невозможно умножить матрицы"
        else:
            for i in range(self.rows):
                for j in range(matrix.cols):
                    for k in range(self.cols):
                        self.data[i][j] += self.data[i][k] * matrix.data[k][j]

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        self.data = result.data

    def __str__(self):
        return '\n'.join([' '.join([str(col) for col in row]) for row in self.data])


m1 = Matrix(2, 3)
m1.data = [[9, 8, 7], [6, 5, 4]]
m2 = Matrix(2, 3)
m2.data = [[1, 2, 3], [4, 5, 6]]
m3 = Matrix(3, 2)
m3.data = [[12, 2], [6, 4], [8, 3]]

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
m1.plus(m2)
print(m1)

print("Вычитание матриц:")
m1.minus(m2)
print(m1)

print("Умножение матриц:")
m1.multiply(m3)
print(m1)

print("Транспонирование матрицы:")
m1.transpose()
print(m1)
