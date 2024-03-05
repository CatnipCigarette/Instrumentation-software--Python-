first = open ('text.txt')
second = open ('output.txt','a')

list_of_numbers = []
list_of_numbers = first.readline().split()
list_of_numbers = list(map(int, list_of_numbers))

factor = 1
for i in list_of_numbers:
    factor *= i
second.write(str(factor))

first.close()
second.close()
