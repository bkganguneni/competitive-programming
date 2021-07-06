t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    for i in range(n//2):
        b.append(a[0])
        b.append(a[-1])
        a.pop(0)
        a.pop(-1)
    b = b+a 
    b.reverse()
    print(*b)
        
    t=t-1
