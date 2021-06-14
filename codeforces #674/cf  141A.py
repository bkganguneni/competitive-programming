a = list(input())
b = list(input())
c = list(input())
d = a+b
d.sort()
c.sort()
e = []
if len(d)!=len(c):
    print("NO")
else:
    for i in range(len(d)):
        if d[i]==c[i]:
            e.append(1)
        else:
            e.append(0)
    if len(set(e))==2:
        print("NO")
    elif len(set(e))==1 and e[0]==0:
        print("NO")
    else:
        print("YES")
