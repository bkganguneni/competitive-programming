n = int(input())
a = []
for i in range(n+1,10001):
    if len(set(str(i)))==4:
        a.append(int(i))
        
        if len(a)==1:
            break
print(a[0])
