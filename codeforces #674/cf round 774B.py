t = int(input())
while t>0:
    s = list(input())
    n = len(s)
    a = [0]*26
    for i in range(n):
        a[ord(s[i])-ord('a')] = a[ord(s[i])-ord('a')]+1
        
    x,y = 0,0
    for i in range(26):
        if a[i]==1:
            x=x+1
        elif a[i]>1:
            y=y+1
    print(x//2 +y)
    
    
    t=t-1
