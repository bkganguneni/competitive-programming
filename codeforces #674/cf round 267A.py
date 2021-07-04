t = int(input())
a=[]
c = 0
for i in range(t):
    p = list(map(int,input().split()))
    a.append(p)
for i in range(t):
    if a[i][1]-a[i][0]>=2:
        c=c+1
print(c)
