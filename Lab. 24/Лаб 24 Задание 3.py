import numpy as np

array = np.random.randint(0,15,10)
print('Одномерный массив:','\n',array)

array = array.reshape(2,5)
print('Двумерный массив:','\n',array)

np.fill_diagonal(array,0)
print('Замена элементов главной диагонали на 0:','\n',array)

