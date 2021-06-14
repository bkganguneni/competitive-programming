n = int(input())
if n%2 == 0:
    print(n//2)
    a = [2 for i in range(n//2)]
    print(*a)
else:
    print((n//2))
    a = [2]*(n//2 - 1)
    a.append(3)
    print(*a)
    
    
