n = int(input())
a = []
b = []
c = []
a = input().split()
for i in range(n):
    a[i] = int(a[i])
    b.append(a[i])
b.sort()
if b == a:
    for i in range(n):
        c.append(i)
else:
    for i in range(n):
        count = 0
        for j in range(n):
            if count == 0 and c.count(j) < 1:
                if b[i] == a[j]:
                    c.append(j)
                    count = 1
print(*c)
