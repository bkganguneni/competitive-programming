t = int(input())
while t>0:
    h,w = map(int,input().split())
    a = [[0 for i in range(w)] for j in range(h)]
    
    for i in range(w):
        if i%2==0:
            a[0][i]=1
        else:
            a[0][i]=0
    for i in range(1,h):
        if i%2==0:
            a[i][w-1]=1
        else:
            a[i][w-1]=0
    for i in range(1,w):
        if i%2==0:
            a[h-1][w-i-1]=1
        else:
            a[h-1][w-i-1]=0
    
    for i in range(1,h-1):
        if i%2==0:
            a[i][0]=1
        else:
            a[i][0]=0
            
    a[h-2][0]=0
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j]=str(a[i][j])
    for i in range(len(a)):
        print("".join(a[i]))
        
            
    
    print(" ")
    t=t-1 
