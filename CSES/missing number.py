n = int(input())
a = list(map(int,input().split()))
x = int((n*(n+1))/2)
print(x-sum(a))