n,q=map(int, input().split())
s=input()
arr=[0]
for x in s:
    arr.append(arr[-1]+(ord(x)-ord('a')+1))
print(arr)
for x in range(q):
    a,b=map(int, input().split())
    print(arr[b]-arr[a-1])
