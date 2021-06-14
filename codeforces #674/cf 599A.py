a = list(map(int,input().split()))
a.sort()
print(min(sum(a),(a[0]+a[1])*2))
