n = int(input())
a = [n]
for i in range(100000):
    if a[0]==1:
        a = [1]
        break
    if n%2 == 0:
        a.append(int(n/2))
    else:
        a.append(n*3+1)
    if a[-1]!= 1:
        n = a[-1]
    else:
        break
print(*a)