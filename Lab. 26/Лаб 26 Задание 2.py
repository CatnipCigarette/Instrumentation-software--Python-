import numpy as np

array = np.random.randint(-10,10,(5,5))
uniq_array = np.unique(array, return_counts = True)[1] == 1
result = np.unique(array) [uniq_array]

print ('Массив:','\n', array)
print ('Встречаются один раз: ', result)
