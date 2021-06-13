a, b = map(int, input().split())
x, y, z = map(int, input().split())
 
yellow = 2 * x + y
blue = y + 3 * z
ans = max(0, yellow - a) + max(0, blue - b)
 
print(ans)
