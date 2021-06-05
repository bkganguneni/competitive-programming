import sys
import math
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]%2==0 or a[j]%2==0 or math.gcd(a[i],a[j])>1:
                s+=1
    print(s)
