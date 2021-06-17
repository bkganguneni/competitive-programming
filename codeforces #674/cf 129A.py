n = int(input())
a = list(map(int,input().split()))
count = 0
if sum(a)%2==1:
    for i in range(n):
        if a[i]%2==1:
            count = count+1
    print(count)
else:
    for i in range(n):
        if a[i]%2==0:
            count = count+1
    print(count)
    
