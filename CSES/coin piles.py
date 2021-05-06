t = int(input())
while t>0:
    a,b = map(int,input().split())
    if (a+b)%3==0 and abs(a - b) <= min(a, b):
        print("YES")
    else:
        print("NO")
    t = t-1