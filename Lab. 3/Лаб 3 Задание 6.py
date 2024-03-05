N = int(input('Введите число N:'))
summ = float(0)
number = float
if N < 101:
for i in range(1, N + 1):
    number = 1 / i
    summ = summ + number
    i = i + 1
    print(summ)
else:
    print('Число больше 100, попробуйте ещё раз')
        
