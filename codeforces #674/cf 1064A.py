a=list(map(int,input().split()))
a.sort()
if a[0]+a[1]>a[2]:
    print(0)
else:
    print(a[2]-a[0]-a[1]+1)
    
