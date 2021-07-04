n,k = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in range(n):
    if a[i]>k:
        c = c+1
print(n+c)
        
