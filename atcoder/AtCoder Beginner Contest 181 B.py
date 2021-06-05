n = int(input())
b = []
c = []
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
    c.append(int((b[i][1]-b[i][0]+1)*(b[i][1]+b[i][0])/2))

print(sum(c))
    