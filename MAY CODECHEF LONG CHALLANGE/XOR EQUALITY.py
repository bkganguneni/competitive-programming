def power(x, y):
    m = 10**9 + 7
    res = 1   
    while (y > 0):
        if ((y & 1) != 0):
            res = res * x % m
        y = y >> 1 
        x = x * x % m  
    return res
 
t = int(input())

while t>0:
    m = 10**9 + 7
    b = int(input())
    print(power(2,b-1)%m)
    
    t = t-1