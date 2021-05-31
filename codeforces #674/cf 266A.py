n = int(input())
a = list(map(str,input()))

c = 0
for i in range(0,len(a)-1):
    if a[i] == a[i+1]:
        a[i] = ''
        c += 1
print(c)
