print('Введите строку для изменения:')
line = input()
print(line[(len(line) + 1) // 2:] + line[:(len(line) + 1) // 2])
