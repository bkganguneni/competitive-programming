t = int(input())
while t>0:
    a = list(input())
    if a[0]!='1':
        a = ['1']+a
    elif a[0]=='1':
        a = [a[0]]+["0"]+a[1:]
    print("".join(a))
    t=t-1
