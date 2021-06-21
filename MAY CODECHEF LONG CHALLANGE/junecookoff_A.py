import bisect
n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
total = 0
while q>0:
    x = int(input())
    pos = bisect.bisect_left(a, x, lo=0, hi=len(a))
    if pos<n and a[pos]==x:
        print(0)
    elif pos%2==0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
    
    q=q-1
