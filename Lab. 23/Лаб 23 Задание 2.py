import numpy as np

array = np.random.uniform(-10,10,(6,7))
np.set_printoptions(precision=1)
print('Двумерный массив:','\n', array)

output = array[0]
print('Первая строка:','\n', output)

opposite = array*-1
print('Замена элементов:','\n', opposite)

length = len(array)
print('Длина массива:', length)

