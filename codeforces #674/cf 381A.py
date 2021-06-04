n = int(input()) 
a = list(map(int,input().split()))
b = []
c = []
for i in range(n):
    if i%2==0:
        b.append(max(a[0],a[-1]))
        a.remove(max(a[0],a[-1]))
    else:
        c.append(max(a[0],a[-1]))
        a.remove(max(a[0],a[-1]))
print(sum(b),sum(c))
    
