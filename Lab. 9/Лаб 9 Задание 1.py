task_list = list(map(int, input('Введите список через пробел:').split()))
moving = int(input('Число шагов: '))

def list_shift(list_, moving):
    if moving > 0:
        list_.append(list_.pop(0))
        moving  -= 1
        list_shift(list_, moving)
    else:
        print(task_list)

print('Исходный список:', task_list)
print('Итоговый список:', end= ' ')
list_shift(task_list, moving)
