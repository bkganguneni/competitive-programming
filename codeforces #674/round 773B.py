q = int(input())
while q>0:
    
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = "NO"
    for i in range(n):
        if s[i]==t[0]:
            x = 0
            y = i
            z = 0
            while(y<n and z<m and s[y]==t[z]):
                x = x+1
                y = y+1
                z = z+1
            y = y-2
            while(y>=0 and z<m and s[y]==t[z]):
                y = y-1
                z = z+1
                x = x+1
            if x==m:
                ans = "YES"
    print(ans)
    q=q-1