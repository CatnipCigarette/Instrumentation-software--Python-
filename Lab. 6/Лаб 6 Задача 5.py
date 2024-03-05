lines, columns = [int(i) for i in input('Введите кол-во строк и столбцов:').split()]
matrix = [[int(j) for j in input('Введите строку матрицы:').split()] for i in range(lines)]

print('Поворот матрицы на 90 градусов: ')
 
rotated = tuple(zip(*matrix[::-1])) 

for i in range(len(rotated)):
    for j in range(len(rotated[i])):
        print(rotated[i][j], end=' ')
    print()
