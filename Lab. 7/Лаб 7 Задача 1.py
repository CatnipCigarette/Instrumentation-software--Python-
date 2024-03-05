import random
first_tuple = tuple(random.randint(0, 5) for i in range(10))
second_tuple = tuple(random.randint(-5, 0) for i in range(10))

final_tuple = first_tuple + second_tuple
number_of_zeros = final_tuple.count(0)

print('Готовый кортеж:', final_tuple)
print('Количество нулей в нём:', number_of_zeros)

_tuple = tuple(random.randint(0, 10) for i in range(number_of_zeros*2))

print(_tuple)
