t = int(input())
while t>0:
    n = list(input())
    for i in range(len(n)):
        n[i]= int(n[i])
    print(max(n))
    t=t-1
