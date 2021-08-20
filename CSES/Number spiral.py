t=int(input())
while t>0:
    y,x = map(int,input().split())
    if x>y:
        if x%2==1:
            print(x*x - y+1)
        else:
            x = x-1
            print(x*x + y)
    else:
        if y%2==0:
            print(y**2 - x+1)
        else:
            y = y-1
            print(y*y +x)
    
    t=t-1