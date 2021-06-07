b=[]
c=[]
for i in range(26):
    c.append(chr(97+i))

for i in c:
    b.append(i)
    for j in c:
        b.append(i+j)
        for k in c:
            b.append(i+j+k)
 
b.sort(key=len)

for _ in range(int(input())):
    n=int(input())
    a=input()
    for i in b:
        if i not in a:
            print(i)
            break
