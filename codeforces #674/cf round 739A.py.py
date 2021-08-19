t = int(input())
while t>0:
    n = int(input())
    a = [i for i in range(1,3000)]
    b = []
    for i in range(len(a)):
        if not (a[i]%3==0 or a[i]%10==3):
            b.append(a[i])
    print(b[n-1])
            
    
    t=t-1