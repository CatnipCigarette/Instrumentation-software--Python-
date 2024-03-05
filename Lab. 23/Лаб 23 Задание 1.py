import numpy as np

initial_array = np.random.randint(-20,20,6)
print('Начальный массив:',initial_array)

opposite_element = initial_array[0] * -1
initial_array[0] = opposite_element
print('Массив с заменой элемента:',initial_array)

search_for_five = 5 in initial_array
if search_for_five:
    print('Элемент равный 5 присутствует в массиве ')
else:
    print('Элемент равный 5 отсутствует в массиве')


modified_array = initial_array.reshape(2,3)
print('Двумерный массив:','\n',modified_array)

shape = modified_array.shape
print('Кол-во строк:', shape[0])
print('Кол-во столбцов:', shape[1])
