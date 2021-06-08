t = int(input())
while t>0:
    n = input()
    a = [1,2,3,4]
    ans = (int(n[0])-1)*10 + sum(a[:len(n)])
    print(ans)
    t = t-1
