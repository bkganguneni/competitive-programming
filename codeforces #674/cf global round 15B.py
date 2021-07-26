t = int(input())
while t>0:
    n = int(input())
    a = []
    for i in range(n):
        x = list(map(int,input().split()))
        a.append(x)
    if n==1:
        print(1)
    else:
        ind = 0
        for i in range(1,n):
            c = 0
            for j in range(5):
                if a[i][j]<a[ind][j]:
                    c=c+1
                if c>=3:
                    ind =  i
                    
        p = True
        for i in range(n):
            c=0
            if i!=ind:
                for j in range(5):
                    if a[ind][j]<a[i][j]:
                        c = c+1
                if c<3:
                    p = False
                    break
        if p:
            print(ind+1)
        else:
            print(-1)
                
    t=t-1
