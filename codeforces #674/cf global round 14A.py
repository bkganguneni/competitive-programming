t = int(input())
while t>0:
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    if (n==1 and a[0]==k) or sum(a)==k:
        print("NO")
    else:
        for i in range(n-1):
            ans = ans+a[i]
            if k == ans:
                a[i],a[i+1]=a[i+1],a[i]
        print("YES")
        print(*a)
        
    t=t-1
