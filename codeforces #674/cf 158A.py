n,k = map(int,input().split())
a = list(map(int,input().split()))
count=0
for i in range(n):
    if a[k-1]==0 and a[i]==0:
        a[i]= -1
        a[k-1]= 0
    else:
        if a[i]>=a[k-1]:
            count = count+1
print(count)
