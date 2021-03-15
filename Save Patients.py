n = int(input())
a = []
a = input()
a = list(map(int,a.split()))
b = []
b = input()
b = list(map(int,b.split()))
if sum(b)>sum(a):
    print("Yes")
else:
    print("No")
