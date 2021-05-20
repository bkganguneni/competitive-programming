t = int(input())
while t>0:
    n = int(input())
    if n==1 or n==2 or n==4 :
        print(-1)
    elif n % 3 == 0:
        print(*[n//3,0,0])
    elif n % 3 == 1:
        print(*[(n-7)//3,0,1])
    else:
        print(*[(n - 5)//3,1,0])
                        
    
                
    t = t-1