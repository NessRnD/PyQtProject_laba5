import random

class MyArray:
    def __init__(self, array=None):
        if array is None:
            self.array = []
        else:
            self.array = array

    def manual_fill(self, array):
        self.array = array

    def auto_fill(self, rows, cols, min_val, max_val):
        self.array = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    def __len__(self):
        if all(isinstance(row, list) for row in self.array):
            # Multidimensional array
            rows = len(self.array)
            cols = len(self.array[0]) if rows > 0 else 0
            print(f"Многомерный массив: длина - {rows} строк, {cols} столбцов")
            return rows
        else:
            # One-dimensional array
            length = len(self.array)
            print(f"Одномерный массив: длина - 1 строка, {length} столбцов")
            return length

    def show(self, separator=' '):
        if all(isinstance(row, list) for row in self.array):
            return '\n'.join([separator.join(f"{elem:.0f}" if isinstance(elem, (int, float)) and elem.is_integer() else f"{elem:.1f}" for elem in row) for row in self.array])
        else:
            return separator.join(f"{elem:.0f}" if isinstance(elem, (int, float)) and elem.is_integer() else f"{elem:.1f}" for elem in self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem + other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Массивы должны быть одной размерности для сложения")
            return MyArray([[self.array[i][j] + other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem - other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Массивы должны быть одной размерности для вычитания")
            return MyArray([[self.array[i][j] - other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem * other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Массивы должны быть одной размерности для умножения")
            return MyArray([[self.array[i][j] * other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem / other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Массивы должны быть одной размерности для деления")
            return MyArray([[self.array[i][j] / other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            result = []
            if all(isinstance(row, list) for row in self.array):
                # Multidimensional array
                for i, row in enumerate(self.array):
                    for j, elem in enumerate(row):
                        if elem > other:
                            result.append((i, j, elem))
            else:
                # One-dimensional array
                for i, elem in enumerate(self.array):
                    if elem > other:
                        result.append((i, elem))
            return result
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Массивы должны быть одной размерности для сравнения")
            result = []
            for i in range(len(self.array)):
                for j in range(len(self.array[i])):
                    if self.array[i][j] > other.array[i][j]:
                        result.append((i, j, self.array[i][j]))
            return result
        else:
            raise TypeError("Unsupported operand type")

    def sort_even(self):
        self.array = [sorted([elem for elem in row if elem % 2 == 0]) for row in self.array]

    def add_element_to_start(self, element):
        if all(isinstance(row, list) for row in self.array):
            self.array[0][0] = element
        else:
            self.array.insert(0, element)

    def remove_element_from_start(self):
        if all(isinstance(row, list) for row in self.array):
            self.array[0][0] = 0
        else:
            if self.array:
                self.array.pop(0)

    def slice(self, *args):
        if all(isinstance(row, list) for row in self.array):
            if len(args) == 4:
                row_start, row_end, col_start, col_end = args
                return MyArray([row[col_start:col_end] for row in self.array[row_start:row_end]])
            else:
                raise ValueError("For multidimensional arrays, provide row_start, row_end, col_start, col_end")
        else:
            if len(args) == 2:
                start, end = args
                return MyArray(self.array[start:end])
            else:
                raise ValueError("For one-dimensional arrays, provide start and end indices")
class MyMatrix(MyArray):
    def count_columns_without_odd_elements(self):
        count = 0
        for col in range(len(self.array[0])):
            if all(elem % 2 != 0 for elem in [row[col] for row in self.array]):
                count += 1
        return count


    def sum_positive_even_elements_in_columns(self):
        result = []
        for col in range(len(self.array[0])):
            sum_positive_even = sum(row[col] for row in self.array if row[col] > 0 and row[col] % 2 == 0)
            if sum_positive_even == 0:
                result.append((col, "Положительные элементы отсутствуют"))
            else:
                result.append((col, sum_positive_even))
        return result

if __name__ == "__main__":

    array1 = MyArray([1, 2, 3, 4, 5])
    print("Array 1 (one-dimensional):")
    print(array1.show())
    print("Length of Array 1:", len(array1))

    array2 = MyArray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Array 2 (two-dimensional):")
    print(array2.show())
    print("Length of Array 2:", len(array2))

    sliced_array1 = array1.slice(1, 4)
    print("Sliced Array 1 (one-dimensional):")
    print(sliced_array1.show())

    sliced_array2 = array2.slice(1, 3, 1, 3)
    print("Sliced Array 2 (two-dimensional):")
    print(sliced_array2.show())

    comparison_result1 = array1 > 3
    print("вывод в формате столбец/элемент который больше заданного числа:")
    print(comparison_result1)

    comparison_result2 = array2 > 3
    print("вывод в формате строка/столбец/элемент который больше заданного числа:")
    print(comparison_result2)

    array3 = MyArray([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    comparison_result3 = array3 > array2
    print("вывод в формате строка/столбец/элемент который больше:")
    print(comparison_result3)

    matrix = MyMatrix()
    matrix.auto_fill(4, 4, -10, 10)
    print("Matrix:")
    print(matrix.show())

    count_columns = matrix.count_columns_without_odd_elements()
    print(f"Количество столбцов, не содержащих ни одного нечетного элемента: {count_columns}")

    sum_positive_even_columns = matrix.sum_positive_even_elements_in_columns()
    print("Сумма положительных четных элементов столбцов:")
    for col in sum_positive_even_columns:
        print(f"Column {col[0]}: {col[1]}")
