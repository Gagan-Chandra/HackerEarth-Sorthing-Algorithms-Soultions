tc = int(input())
c = []
for i in range(tc):
    a = []
    a = input().split()
    for i in range(1,2):
        a[i] = int(a[i])
    c.append(a)
maxi =- 1
for i in range(len(c)):
    m = c[i][1]
    if len(c[i][0]) <= 20:
        if m > maxi:
            maxi = m
            order = c[i][0]
        elif c[i][1] == maxi:
            order = min(c[i][0],order)
print(order)
