n,m=map(int,input().split())
x=input()
while m:
	x=x.replace("BG","GB")
	m-=1
print (x)