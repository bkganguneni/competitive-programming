n = int(input())
a = []
b = []
for i in range(n):
    c,d = map(int,input().split())
    a.append(c)
    b.append(d)
a.sort()
b.sort()

maximum = 0 
current = 0
i,j = 0,0
while i<n and j<n:
    if a[i]<b[j]:
        current = current+1
        i = i+1
    else:
        current = current-1
        j = j+1
    
    if maximum<current:
        maximum=current
        
print(maximum)
    
    
