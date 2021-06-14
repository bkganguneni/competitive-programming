a,b = map(int,input().split())
print(min(a,b),max((a-min(a,b))//2,(b-min(a,b))//2))
