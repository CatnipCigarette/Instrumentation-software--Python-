numbers = [int(i) for i in input().split()]
previously_met = set()
for i in numbers:
    if i in previously_met:
        print('YES')
    else:
        print('NO')
        previously_met.add(i)
