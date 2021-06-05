t = int(input())
while t>0:
    a = list(map(int,input().split()))
    b = [max(a[0],a[1]),max(a[2],a[3])]
    a.sort()
    b.sort()
    a = a[2:]
    if a==b:
        print("YES")
    else:
        print("NO")
    t = t-1
