# # Задача 3.1.
# # Создайте класс матрицы (или таблицы).
# # Требования к классу:
# #   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
# #   - в каждой ячейке содержится либо число, либо None
# #   - доступы следующие методы матрицы:
# #       * принимать новые значения, 
# #       * заменять существующие значения, 
# #       * выводить число строк и колонок.

# # Пример матрицы 10 на 10 из единиц:
# # [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# # Примечание! 
# #   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
# #   - отображать в таблице/матрице название колонки не обязательно!
# #   - проявите фантазию :)


class Matrix:
    def __init__(self, rows, cols, fill_value=1):
        self.rows = rows
        self.cols = cols
        self.matrix = [[fill_value for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
        else:
            raise IndexError("Выход за границы матрицы")

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            raise IndexError("Выход за границы матрицы")

    def replace_value(self, row, col, new_value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = new_value
        else:
            raise IndexError("Выход за границы матрицы")

    def dimensions(self):
        return self.rows, self.cols

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            row_str = " ".join([str(val) for val in row])
            matrix_str += row_str + "\n"
        return matrix_str


if __name__ == "__main__":
    my_matrix = Matrix(10, 11, fill_value=10)
    print(my_matrix)

    my_matrix.set_value(0, 9, 2)
    print(my_matrix)

    my_matrix.replace_value(0, 1, 100)
    print(my_matrix)

    print("Размер матрицы:", my_matrix.dimensions())
