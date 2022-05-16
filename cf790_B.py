t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(1,len(a)):
        ans = ans+ a[i]-a[0]
    print(ans)
    t=t-1
