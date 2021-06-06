n,l = map(int,input().split())
a = [input() for i in range(n)]
b = ""
a.sort()
for i in range(n):
    b = b+a[i]
print(b)
