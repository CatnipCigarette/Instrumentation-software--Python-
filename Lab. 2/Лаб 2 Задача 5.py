import math
print('Введите коэффициенты для уравнения')
print('ax^2+bx+c=0:')
a=int(input('Введите коэффицент a:'))
b=int(input('Введите коэффицент b:'))
c=int(input('Введите коэффицент c:'))
D=b**2-4*a*c
print(D)
if D > 0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print(x1, x2)
elif D == 0:
    x=-b/(2*a)
    print(x)
else:
    print('Корней нет')
