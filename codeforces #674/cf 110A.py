n = list(input())
count = 0
for i in range(len(n)):
    if n[i]=='4' or n[i]=='7':
        count = count+1
a = str(count)
b = ['4','7']
c = []
for i in range(len(a)):
    if a[i] in b:
        c.append(1)
    else:
        c.append(0)
if len(c)==2:
    print("NO")
elif len(c)==1 and c[0]==0:
    print("NO")
else:
    print("YES")
