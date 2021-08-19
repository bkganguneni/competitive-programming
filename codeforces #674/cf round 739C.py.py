t = int(input())
while t>0:
    n,k = map(int,input().split())
    a = list(str(n))
    for i in range(len(a)):
        a[i] = int(a[i])
    if len(set(a))==k:
        print(n)
    else:
        if k==1:
            if max(a)!=a[0]:
                a = [a[0]+1]*len(a)
            else:
                a = [a[0]]*len(a)
        if k ==2:
            for i in range(len(a)-1,0,-1):
                if a[i]>a[i+1]:
                    
            
            
        
        for i in range(len(a)):
            a[i] = str(a[i])
        print("".join(a))
        
            
        
        
    t=t-1