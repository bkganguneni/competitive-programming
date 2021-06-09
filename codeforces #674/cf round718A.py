t = int(input())
while t>0:
    a = []
    n = int(input())
    if n%2050 !=0:
        print(-1)
    else:
        ans = list(str(n//2050))
        for i in ans:
            a.append(int(i))
        print(sum(a))
        
    
    t=t-1
