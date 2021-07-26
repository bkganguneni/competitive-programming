t = int(input())
while t>0:
    n = int(input())
    s = list(input())
    a = s.copy()
    a.sort()
    ans = 0
    for i in range(n):
        if a[i]!=s[i]:
            ans = ans+1
    print(ans)
    
    
    t=t-1
