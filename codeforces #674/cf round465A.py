n = int(input())
a = []
if n<4:
    print(1)
else:
    for i in range(1,int(n//2)+1):
        if n%i==0:
            a.append(i)
    print(len(a))
