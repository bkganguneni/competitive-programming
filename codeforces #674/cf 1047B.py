n = int(input())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
    a[i] = sum(a[i])
print(max(a))
