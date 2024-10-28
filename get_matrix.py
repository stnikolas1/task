n = int(input('Введите количество строк '))
m = int(input('Введите количество столбцов '))
value = input('Введите значение для заполнения матрицы ')
matrix = []
def get_matrix(n, m, value):
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result_1 = get_matrix(n, m, value)
print(result_1)