a=int(input("введите переменную a:"))
b=int(input("введите переменную b:"))
c=((a+b)*((a**2)-b))/3
print("результат - 1=",c)
vibor=input("в какую систему перевести? в десятичную или двоичную?\n")
if vibor=="двоичную":
    n=int(input("введите ваше число\n"))
    print(bin(n))
if vibor=="десятичную":
    n=input("введите ваше число\n")
    print(int(n, 2))
    
    



























               
