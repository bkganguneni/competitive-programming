t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    odd = 0
    even = 0
    for i in range(n):
        if a[i]%2 == 0:
            even+=1
        else:
            odd+=1
    if odd!= n//2:
        print(-1)
    else:
        ans = 0
        for i in range(n):
            if a[i]%2 != i%2:
                ans+=1
        print(ans//2)
        
        
    t=t-1
