import numpy as np

array = np.random.randint(1,6,(8,9))
min_element = np.argmin(array)
max_element = np.argmax(array)

print('Матрица:')
print(array, '\n')
print('Индекс минимального элемента:', min_element)
print('Индекс максимальный элемента:', max_element, '\n')

min_element = (np.unravel_index(min_element, array.shape))
max_element = (np.unravel_index(max_element, array.shape))
array[max_element], array[min_element] = array[min_element], array[max_element]

print('Полученная матрица:')
print(array)




 
