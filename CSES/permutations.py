# cook your dish here
n = int(input())
a = []
b = []
if n == 1:
    a = [1]
    
elif n == 4:
    a = [2,4,1,3]
elif n==2 or n==3:
    print("NO SOLUTION")
else:
    for i in range(1,n+1):
        if i%2!=0:
            a.append(i)
        else:
            b.append(i)
print(*(a+b))