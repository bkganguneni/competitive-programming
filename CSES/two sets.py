# cook your dish here
n = int(input())
total = n*(n+1)//2
a = []
b = []
target = total//2
if total%2==0:
    print("YES")
    for i in range(n,0,-1):
        if i<=target:
            b.append(i)
            target = target - i
        else:
            a.append(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
    
        
else:
    print("NO")
    