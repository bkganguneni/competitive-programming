t = int(input())
while t>0:
    n,k = map(int,input().split())
    if k>n:
        print(k-n)
    elif n % 2 == k % 2:
        print(0)
    else:
        print(1)
    t = t-1