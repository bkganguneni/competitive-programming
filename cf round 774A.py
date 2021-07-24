t = int(input())
while t>0:
    n = int(input())
    if n%3==0:
        print(n//3,n//3)
    elif n%3==1:
        print(n//3 +1,n//3)
    else:
        print(n//3,n//3 +1)
            
    t=t-1
