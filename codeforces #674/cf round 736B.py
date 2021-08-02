t = int(input())
while t>0:
    n = int(input())
    a = list(input())
    b = list(input())
    ans = 0
    for i in range(n):
        if b[i]=='1' and a[i]=='0':
            a[i]=='2'
            ans = ans+1
        elif a[i-1]=='1' and b[i]=='1' and i>0:
            ans = ans+1
            a[i-1]='2'
        elif i < (n-1) and a[i+1]=='1' and b[i]=='1':
            ans = ans+1
            a[i+1]='2'
    print(ans)
    
    t=t-1
