import math
t = int(input())
while t>0:
    n = int(input())
    s = int(n**0.5)
    if s**2 == n:
        print(s,1)
    else:
        if (s**2)-s+1<=n<=s**2:
            print(s,s**2-n)
        elif (s+1)**2-s+1<=n<=(s+1)**2:
            print(s+1,(s+1)**2-n+1)
        else:
            print(n-s**2,s+1)
            
    t=t-1