t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    if a[0]%2==0: 
        print(1)
        print(1)
    elif n==1:
        print(-1)
    elif a[1]%2==0:
        print(1)
        print(2)
    else:
        print(2)
        print(1,2)
    
    t=t-1
