# ДЗ "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):                 # П1
    matrix = []                              # П2
    for i in range(n):                       # П3
        matrix.append([])                    # П4
        for j in range(m):                   # П5
            matrix[i].append(value)          # П6
    print(matrix)
    return matrix                            # П7

n = int(input('Задайте количество строк матрицы : '))
m = int(input('Задайте количество столбцов матрицы : '))
value = input(f'Задайте значения матрицы : ')

matrix = get_matrix(n, m, value)              # П8



