first = open ('text.txt')
second = open ('output.txt','a')

list_of_numbers = []
list_of_numbers = first.readline().split()
list_of_numbers = list(map(int, list_of_numbers))

mini = min(list_of_numbers)
maxi = max(list_of_numbers)

second.write(str(maxi))
second.write(str(' '))
second.write(str(mini))

first.close()
second.close()
