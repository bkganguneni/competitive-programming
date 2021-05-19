t = int(input())
while t>0:
    n,x = map(int,input().split())
    a = [2]
    while n>a[-1]:
        a.append(a[-1]+x)
    print(len(a))
    t = t-1