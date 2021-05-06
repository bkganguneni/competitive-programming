t = int(input())
a,b=0,1
for i in range(t):
    a,b=b,(a + b)*i % (10**9 + 7)
print(b)