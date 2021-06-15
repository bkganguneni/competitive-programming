k,r = map(int,input().split())
a = []
for i in range(1,11):
    if str(k*i)[-1]==str(r) or str(k*i)[-1]==str(0) :
        a.append(i)
print(a[0])
    
