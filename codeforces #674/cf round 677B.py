t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if a[i]==1:
            b.append(i)
    a = a[min(b):max(b)+1]
    print(a.count(0))
    t = t-1
