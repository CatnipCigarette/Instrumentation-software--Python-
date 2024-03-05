natural_number = int(input('Введите число:'))
sum_of_numders = 0
product_of_numbers = 1
while natural_number > 0:
    number = natural_number % 10
    sum_of_numders = sum_of_numders + number
    product_of_numbers = product_of_numbers * number
    natural_number = natural_number // 10
print('Сумма всех цифр числа:', sum_of_numders)
print('Произведение всех цифр числа:', product_of_numbers)
