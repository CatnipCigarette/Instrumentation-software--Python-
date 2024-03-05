import math
x=int(input('Введите x:'))
if x < 0:
    y=math.sin(x)+9*math.cos(x)
elif 0 < x < 8:
    y=4*math.pi+x
elif x == 0:
    y=math.sin(x) + 9*math.cos(x) 
else:
    y=0
print(y)
