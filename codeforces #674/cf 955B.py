
n = int(input())
a = input()
x = 0
y = 0
t = 0
for i in range(n-1):
    if a[i]=='U':
        y+=1
    else:
        x+=1
    if x==y and a[i]==a[i+1]:
        t+=1
print(t)
