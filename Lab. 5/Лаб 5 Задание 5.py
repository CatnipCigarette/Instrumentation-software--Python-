from random import randint
mini=int(input('Введите заданный минимум: '))
maxi=int(input('Введите заданный максимум: '))
list_length=int(input('Введите размер списка:'))
start_random = int(input('Введите минимально возможное число списка:'))
end_random = int(input('Введите максимально возможное число списка: ') )

random_list =[randint(start_random, end_random) for i in range(list_length)]
counting = 0

for i in random_list:
    if maxi >= i >= mini:
       counting  += 1
        
print(random_list)
print('Количество чисел в диапазоне от', mini, 'до', maxi, 'равно:', counting)
