my_list= [[i * j for j in range (6)] for i in range (5)]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')
    print()    
