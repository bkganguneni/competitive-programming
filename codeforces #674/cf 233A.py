n = int(input())
a = [i for i in range(1,n+1,2)]
b = [i for i in range(2,n+1,2)]
c = []
if n%2==1:
    print(-1)
else:
    for i in range(n):
        if i%2==0:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
print(*c)
