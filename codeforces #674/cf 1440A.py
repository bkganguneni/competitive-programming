t = int(input())
while t>0:
    n,c0,c1,h = map(int,input().split())
    s = input()
    ans = 0
    
    for i in range(n):
        if s[i] == '0':
            ans = ans + min(c0,h+c1)
        else:
            ans = ans+min(c1,c0+h)
    
    print(ans)
    t=t-1
