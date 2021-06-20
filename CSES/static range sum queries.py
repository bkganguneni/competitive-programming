n,k = map(int,input().split())
a = list(map(int,input().split()))
a.insert(0,0)
for i in range(1,n+1):
    a[i]= a[i]+a[i-1]
while k>0:
    m,n = map(int,input().split())
    print(a[n]-a[m-1])
    k = k-1
