from random import randint
task_list = [randint(-10, 10) for i in range(10)]

number_repetition = [item for item in set(task_list) if task_list.count(item) > 1]

print(task_list)
print(number_repetition)
