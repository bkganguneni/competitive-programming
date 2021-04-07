# cook your dish here
import math as mt
t = int(input())
while t>0:
    n = list(map(int,input().split()))
    a = n[0]
    if a == 3:
        c = round((4/3),8)
        print(c)
    else:
        b = (2 * mt.cos((((a - 2) * 180) /(2 * a)) * 3.14159 / 180))
        print(round(b**2,8))
    
    
            
    t = t-1