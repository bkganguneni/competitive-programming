n = int(input())
a = 0
if n-10<=0 or n-10>11:
    print(0)
else:
    a = n-10
    if 1<=a<=9:
        print(4)
    elif a==10:
        print(15)
    elif a==11:
        print(4)
    
