n = 4
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)
    print(a[i])
for row in a:
    print(' '.join([str(elem) for elem in row]))
