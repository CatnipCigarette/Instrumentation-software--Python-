import numpy as np

array = np.random.randint(1,6,9)
min_element_index = np.argmin(array)
max_element_index = np.argmax(array)

print('Одномерный массив:',array)

if max_element_index > min_element_index:
    sum_of_element = np.sum(array[min_element_index:max_element_index+1])
if max_element_index < min_element_index:
    sum_of_element = np.sum(array[max_element_index+1:min_element_index])
    
print ("Сумма элементов: ", sum_of_element)
