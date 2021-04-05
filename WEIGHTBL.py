# cook your dish here
t = int(input())
x = 0
while t>0:
    
    a = list(map(int,input().split()))
    b = a[1]-a[0]
    c = a[2]*a[4]
    d = a[3]*a[4]
    if c<= b <= d:
        print(1)
    else:
        print(0)
            
   
    t=t-1
