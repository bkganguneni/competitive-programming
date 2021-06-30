import math
n = int(input())
a = list(map(int,input().split()))
a.sort()
a = a[::-1]
t = sum(a)
x = sum(a)/2
count = 0
while t>=x:
    t = t - a[0]
    count = count+1
    a.pop(0)
print(count)
