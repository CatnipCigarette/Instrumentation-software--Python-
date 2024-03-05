import numpy as np

array = np.random.randint(-40,16,(3,3))
max_element = np.amax(array)
array_abs = np.abs(array)
count = np.sum(array_abs > max_element)

print('Матрица:')
print(array)
print('Максимальный элемент: ', max_element)
print('Кол-во элементов по модулю больших, чем максимальный:', count)
