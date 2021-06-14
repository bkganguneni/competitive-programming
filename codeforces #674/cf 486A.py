n = int(input())
a = [i for i in range(1,n+1)]
for i in range(n):
    if a[i]%2==1:
        a[i] = -a[i]
print(sum(a))
