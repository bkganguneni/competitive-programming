n = int(input())
a = list(map(int,input().split()))
count = 0
max = 0
for i in range(n-1):
    if a[i]<=a[i+1]:
        count = count+1
        if count>max:
            max = count
    else:
        count = 0
        

print(max+1)
