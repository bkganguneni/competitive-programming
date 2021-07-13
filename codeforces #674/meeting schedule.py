s = [1,4,0,6,9,10]
f = [3,5,7,8,11,12]
meet = []
ans = []
for i in range(len(s)):
    c = []
    a = s[i]
    b = f[i]
    c.append(a)
    c.append(b)
    meet.append(c)
    
meet.sort(key = lambda x:x[1])
ans.append(meet[0])
c = 1
prev = meet[0][1]
for i in range(1,len(meet)):
    if meet[i][0]>prev:
        prev = meet[i][1]
        c = c+1
print(c)
