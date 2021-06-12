n = int(input())
a = list(map(int,input().split()))
x = 0
b = []
c = []
d = []
e = []
f = []
for i in range(n):
    x = a[i]/2
    b.append(x)
b.sort()

if n%2!=0:
    x = b[(n-1)//2]
    for i in range(n):
        c.append(x+a[i]-min(a[i],2*x))
    print(sum(c)/n)

else:
    for i in range(n):
        x = b[(n-2)//2]
        c.append(x+a[i]-min(a[i],2*x))
    f.append(sum(c)/n)

    for i in range(n):
        x = b[((n-2)//2)+1]
        d.append(x+a[i]-min(a[i],2*x))
    f.append(sum(d)/n)


    for i in range(n):
        x = (b[(n-2)//2]+b[((n-2)//2)+1])/2
        e.append(x+a[i]-min(a[i],2*x))
    f.append(sum(e)/n)
    s = str(min(f))
    x = 0
    for i in range(len(s)):
        if s[i] == ".":
            x = len(s[i+1:])
    s = s + (20-x)*'0'
    print(s)
            
