t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n-1):
        if a[i]%2 !=0:
            a[i],a[n-1] = a[n-1],a[i]
    print(*a)
    t=t-1
