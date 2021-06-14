a = int(input())
b = int(input())
c = abs(a-b)
x = 0
if c%2==0:
    x = c//2
    print(x*(x+1))
else:
    x = c//2
    print(x*(x+1)+(c//2)+1)
    
    
