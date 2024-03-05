import math
menu = 1
while menu == 1:
    first_number = int(input('Введите первое число:'))
    second_number = int(input('Введите второе число:'))
    print('Выберите действие:')
    print('Сложение - 1')
    print('Вычитание - 2')
    print('Умножение - 3')
    print('Деление - 4')
    print('Возведение первого числа в степень второго - 5')
    print('Выделение квадратного корня обо6их чисел - 6')
    print('Перевод в двоичную систему счисления обоих чисел - 7')
    action = int(input('Что выполнить?:'))
    if action == 1:
        result = first_number + second_number
        print('Результат:', result)
    elif action == 2:
        result = first_number - second_number
        print('Результат:', result)
    elif action == 3:
        result = first_number * second_number
        print('Результат:', result)
    elif action == 4:
        result = first_number / second_number
        print('Результат:',result)
    elif action == 5:
        result = first_number ** second_number
        print('Результат:', result)
    elif action == 6:
        result_1 = math.sqrt(first_number)
        result_2 = math.sqrt(second_number)
        print('Результат:',result_1, result_2)
    elif action == 7:
        result_1 = bin(first_number)
        result_2 = bin(second_number)
        print('Результат:', result_1, result_2)
    else:
        print('Такого действия не существует')
    ext=int(input('Выйти?(Да-1 Нет-2):'))
    if ext == 2:
        continue
    else:
        break
