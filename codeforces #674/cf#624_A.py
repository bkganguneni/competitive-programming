t = int(input())
while t>0:
    a,b = map(int,input().split())
    if a==b:
        print(0)
    else:
        print(1 + int((a < b) ^ ((b - a) & 1)))
    t = t-1