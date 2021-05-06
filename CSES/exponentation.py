t = int(input())
while t>0:
    a,b = map(int,input().split())
    m = 10**9 + 7
    def exponential(a,b):
        if a==0 and b==0:
            return 1
        elif a==0 and b!=0:
            return 0
        elif a!=0 and b==0:
            return 1
            
        temp = exponential(a,b//2)
        if b%2!=0:
            ans = temp*temp*a
        else:
            ans = temp*temp
        return ans % m
    print(exponential(a,b))
    t = t-1
