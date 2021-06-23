s = int(input())
while s>0:
    n,x,t = map(int,input().split())
    val = min(n-1,t//x)
    if val==0:
        print(0)
    else:
        summ=max(0,val*(val-1)//2)+val*(n-val)
        print(summ)
    s = s-1
