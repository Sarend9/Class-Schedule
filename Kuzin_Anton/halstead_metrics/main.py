def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply_matrices(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def find_max_in_matrix(matrix):
    max_value = matrix[0][0]
    max_position = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)
    return max_value, max_position


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    AT = transpose(A)
    C = multiply_matrices(A, B)
    max_val, max_pos = find_max_in_matrix(C)

    print("Исходная матрица A:", A)
    print("Исходная матрица B:", B)
    print("Транспонированная матрица A:", AT)
    print("Результат умножения A и B:", C)
    print(f"Максимальный элемент в C: {max_val} на позиции {max_pos}")
