for_first = open('task.txt')
for_second = open('complete task.txt', 'w')

a = [] 
a = for_first.readline().split()
a = list(map(int, a))
a.sort()
for_second.write(str(a))

for_first.close()
for_second.close()

