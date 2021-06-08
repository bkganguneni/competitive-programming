t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    if len(a)==1:
        print("YES")
    else:
        for i in range(n-1):
            if a[i+1]-a[i]>1:
                b.append(1)
            else:
                b.append(0)
        if len(set(b))==2:
            print("NO")
        elif len(set(b))==1 and b[0]==1:
            print("NO")
        else:
            print("YES")
            
    t=t-1
