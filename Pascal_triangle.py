N = 24
P = []

# Строим треугольник Паскаля
for i in range(0, N):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)

# Находим максимальную ширину последней строки (для центрирования)
last_row_str = ' '.join(map(str, P[-1]))
max_width = len(last_row_str)

# Выводим с отступами
for i, row in enumerate(P):
    # Превращаем строку в текст через пробел
    row_str = ' '.join(map(str, row))
    # Вычисляем отступ: (макс_ширина - текущая_ширина) // 2
    # Но проще: центрируем по максимальной ширине
    print(row_str.center(max_width))