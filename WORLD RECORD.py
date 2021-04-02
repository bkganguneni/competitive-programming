t = int(input())
while t>0:
    a,b,c,v = list(map(float,input().split()))
    x = round(100/(a*b*c*v),2)
    if x >= 9.58 :
        print("NO")
    else:
        print("YES")
    t = t-1