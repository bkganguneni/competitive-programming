n,k = map(int,input().split())
a = sorted([list(map(int,input().split())) for _ in range(n)])
money = k
for i in a:
    if(i[0] <= money):
        money += i[1]
    else:
        print(money)
        exit()
print(money)