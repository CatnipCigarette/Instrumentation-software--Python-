import numpy as np

array = np.random.randint(-20,-1,(3,4))
print('Двумерный массив:','\n',array)

sum_of_elements = array.sum(axis=0)
print('Сумма элементов в каждом столбце:','\n',sum_of_elements)

min_element = np.argmin(sum_of_elements) + 1
print('Номер столбца с минимальной суммой:','\n',min_element)
