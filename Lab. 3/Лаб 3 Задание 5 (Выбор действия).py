import math
flag = True
while flag:
    first_number = int(input('Введите первое число:'))
    second_number = int(input('Введите второе число:'))
    print('Выберите действие:')
    print('+, -, *, /, **, sqrt, bin')
    action = input('Что выполнить?:')
    if action == '+':
        result = first_number + second_number
        print('Результат:', result)
    elif action == '-':
        result = first_number - second_number
        print('Результат:', result)
    elif action == '*':
        result = first_number * second_number
        print('Результат:', result)
    elif action == '/':
        result = first_number / second_number
        print('Результат:',result)
    elif action == '**':
        result = first_number ** second_number
        print('Результат:', result)
    elif action == 'sqrt':
        result_1 = math.sqrt(first_number)
        result_2 = math.sqrt(second_number)
        print('Результат:',result_1, result_2)
    elif action == 'bin':
        result_1 = bin(first_number)
        result_2 = bin(second_number)
        print('Результат:', result_1, result_2)
    else:
        print('Такого действия не существует')
    ext=input('Выйти?(да/нет):')
    if ext == 'да':
        flag = False
