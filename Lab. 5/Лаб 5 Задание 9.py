list_size = int(input('Введите размер списка:'))
task_list = []

for i in range(list_size):
    task_list.append(float(input('Введите элемент списка:')))

if task_list == task_list [::-1]:
    print('Список симметричный')
else:
    print('Список не симметричный')
