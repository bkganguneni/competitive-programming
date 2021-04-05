# cook your dish here
t = int(input())
while t>0:
    u,v,a,s = map(int,input().split())
    x = u**2-2*a*s
    if x<v**2:
        print("YES")
    elif  x**0.5== float(v):
        print("YES")
    else:
        print("NO")
    
    t = t-1