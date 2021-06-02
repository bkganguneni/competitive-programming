for _ in range(int(input())):
    n=int(input())
    an=list(map(int,input().split()))
    if sum(an)%2==1:
        print('NO')
 
    elif an.count(1)%2==1:
        print('NO')
    elif an.count(2)%2==0:
        print('YES')
    elif an.count(1)-2>0 :
        print('YES')
    elif an.count(1)%2==0 and an.count(1)!=0:
        print('YES')
 
    else:
        print("NO")
