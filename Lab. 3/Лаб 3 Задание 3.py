number = int(input('Введите число:'))
odd = 0
even = 0
while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number //= 10
print('Нечётных цифр:', odd)
print('Чётных цифр:', even)
