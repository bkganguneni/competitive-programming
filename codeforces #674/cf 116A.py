n = int(input())
a = []
b = []
for i in range(n):
    c,d = map(int,input().split())
    a.append(-c)
    b.append(d)
f = []
e= []
for i in range(n):
    e.append(a[i]+b[i])
    f.append(sum(e[:i+1]))
print(max(f))
