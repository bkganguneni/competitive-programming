t = int(input())
while t>0:
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a)==k:
        print("YES")
    else:
        print("NO")
    t=t-1
