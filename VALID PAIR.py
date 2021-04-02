a = list(map(int,input().split()))
b = list(set(a))

if len(a)==len(b):
    print("NO")
else:
    print("YES")