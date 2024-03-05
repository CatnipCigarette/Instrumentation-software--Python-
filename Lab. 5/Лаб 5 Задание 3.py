list_size = int(input('Введите размер списка:'))
task_list = []

for i in range(list_size):
    task_list.append(float(input('Введите элемент списка:')))
    amount_negative_numbers = 0
    sum_negative_numbers = 0
    minm_item = task_list.index(min(task_list))

for i in task_list:
    if i < 0:
        amount_negative_numbers += 1
        sum_negative_numbers += i

average = sum_negative_numbers / amount_negative_numbers

task_list[minm_item] = average
print(task_list)

  

