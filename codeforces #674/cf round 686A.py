t = int(input())
while t>0:
    n = int(input())
    a= [i for i in range(1,n+1)]
    b = [a[-1]] + a[:n-1]
    print(*b)
    t=t-1
