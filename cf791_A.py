t = int(input())
while t>0:
    n = int(input())
    if n%2 != 0 or n<4:
		print(-1)
	else:
		print((n+4)//6,n//4)
        
    t=t-1
