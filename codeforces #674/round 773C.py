t = int(input())
while t>0:
    s = input()
    odd,even,x,y=0,0,0,0
    n=len(s)
    ans = 10
    for i in range(n):
        if i%2==0:
            if s[i]=='1':
                even = even+1
            elif s[i]=="?":
                x = x+1
        else:
            if s[i]=='1':
                odd = odd+1
            elif s[i]=="?":
                y = y+1
                
        if odd+y>even+(9-i)/2:
            ans = i+1
            break
        if even+x > odd + (10-i)/2:
            ans = i+1
            break
    print(ans)
            
    t=t-1