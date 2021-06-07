n = int(input())
a = [list(map(str, input().split())) for _ in range(n)]
print(a)
x = input()
ans = 0
for i in range(n):
    if a[i][0] == x:
        y = i
for j in range(y+1, n):
    ans += int(a[j][1])
print(ans)
