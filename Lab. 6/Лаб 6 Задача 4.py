lines, columns = [int(i) for i in input('Введите кол-во строк и столбцов:').split()]
matrix = [[int(j) for j in input().split()] for i in range(lines)]

element = matrix[0][0]
for i in range(lines):
    for j in range(columns):
        if matrix[i][j] > element:
            element  = matrix[i][j]
            line_number, column_number = i+1, j+1
            
print(line_number, column_number)
