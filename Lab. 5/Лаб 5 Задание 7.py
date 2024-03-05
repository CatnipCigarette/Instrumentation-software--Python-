list_size=int(input('Введите размер списка:'))
task_list = []

for i in range(list_size):
  task_list.append(float(input('Введите элемент списка:')))
maxi = task_list.index(max(task_list))
mini = task_list.index(min(task_list))

task_list[mini], task_list[maxi] = task_list[maxi], task_list[mini]
print(task_list)
