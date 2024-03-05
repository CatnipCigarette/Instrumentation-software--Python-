import numpy as np

first_array = np.random.randint(1,15,(3,4))
second_array = np.random.randint(1,15,(3,4))

sum_of_matrix = (first_array.T + second_array.T)
product_of_matrix = first_array * second_array
first_sum = np.sum(first_array)
second_sum = np.sum(second_array)
comparison_of_matrix = first_sum > second_sum
    
print(' Первый массив:')
print(first_array)
print('\n','Второй массив:')
print(second_array)
print('\n','Сумма транспонированных матриц:')
print(sum_of_matrix)
print('\n','Произведение матриц:')
print(product_of_matrix)

if comparison_of_matrix:
    print('\n','Сумма второй матрицы меньше')
else:
    print('\n','Сумма первой матрицы меньше')
