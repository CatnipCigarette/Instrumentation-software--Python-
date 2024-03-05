import numpy as np

array = np.random.randint(-5,11,8)
positive_elements = np.count_nonzero(array > 0)
negative_elements = np.count_nonzero(array < 0)
zero_elements = np.count_nonzero(array == 0)

print('Массив:', array)
print('Количество положительных значений:', positive_elements)
print('Количество отрицательных значений:', negative_elements)
print('Количество нулей:', zero_elements)
