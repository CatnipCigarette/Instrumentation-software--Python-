for_first = open('text.txt')
for_second = open('complete task.txt', 'w')

a = [] 
a = for_first.readline().split()
a = list(map(int, a[1]))
for_second.write(str(a))

for_second.close()
