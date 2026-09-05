def deep(matrix, l, r):
    if l == r:
        return 0
    m = 9999999999999999999999999999999
    for k in range(l, r):
        left = deep(matrix, l, k)
        right = deep(matrix, k + 1, r)
        c = matrix[l] * matrix[k + 1] * matrix[r + 1]
        count = left + right + c
        m = min(m, count)
    return m

a = int(input("Количество матриц: "))
matrix = []
for i in range(a):
    m, n = map(int, input(f"Размеры матрицы {i+1}: ").split())
    if i == 0:
        matrix.append(m)
    matrix.append(n)
print(deep(matrix, 0, a - 1))