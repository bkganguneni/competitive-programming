n,k = map(int,input().split())
a = []
 
for i in range(1,n+1):
    for j in range(1,k+1):
        p = (100*i) + j
        a.append(p)
print(sum(a))
