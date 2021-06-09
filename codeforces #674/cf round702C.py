t = int(input())
while t>0:
    n = int(input())
    a = []
    for i in range(1,int(pow(n,1/3))+1):
        a.append(i**3)
    ans = "NO"
    for i in a:
        if n-i in a:
            ans = "YES"
    print(ans)
    
    
    t=t-1
