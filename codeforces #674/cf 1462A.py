t = int(input())
while t>0:
    n = int(input()) 
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if i%2==0:
            b.append(a[0])
            a.pop(0)
        else:
            b.append(a[-1])
            a.pop(-1)
    print(*b)
    t = t-1
