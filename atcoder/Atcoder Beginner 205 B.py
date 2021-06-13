n = int(input())
a = list(map(int,input().split()))
b = [i for i in range(1,n+1)]
a.sort()
if a==b:
    print("Yes")
else:
    print("No")
