t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans = ans + max(a[i]-min(a),b[i]-min(b))
    print(ans)
    
    t=t-1
