t = int(input())
while t>0:
    a,b = map(int,input().split())
    if a%b==0:
        print("YES")
    else:
        print("NO")
    
    t=t-1
