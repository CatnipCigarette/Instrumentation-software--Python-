x=int(input('Введите x:'))
if x > 0:
    y=2*x-10
elif x == 0:
    y=0
elif x < 0:
    y=abs(x)*2-1
print(y)
