tc = int(input())
c = []
for i in range(tc):
    sum_min = 0
    sum_max = 0
    b = []
    b = input().split()
    for i in range(2):
        b[i] = int(b[i])
    a = []
    a = input().split()
    for i in range(b[0]):
        a[i] = int(a[i])
    a.sort()
    for i in range(b[0] - b[1]):
        sum_min = sum_min + a[i]
    a.reverse()
    for i in range(b[0] - b[1]):
        sum_max = sum_max + a[i]
    x = sum_max - sum_min
    c.append(x)
for e in c:
    print(e)
