def gcd(a,b):
    if b>a:
        a,b = b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)


t = int(input())
while t>0:
    k = int(input())
    x = 100-k
    ans = (k/gcd(k,x))+(x/gcd(k,x))
    print(int(ans))
        
    t = t-1