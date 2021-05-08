n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(1,n):
    if a[i-1]>a[i]:
        count = count + (a[i-1]-a[i])
        a[i]=a[i-1]
        
print(count)