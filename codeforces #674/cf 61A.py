a = input()
b = input()
n = len(a)
ans = []
for i in range(n):
    if a[i]=='1' and b[i]=='1':
        ans.append('0')
    elif (a[i]=='1' and b[i]=='0'):
        ans.append('1')
    elif (a[i]=='0' and b[i]=='1'):
        ans.append('1')
    else:
        ans.append('0')
print("".join(ans))
    
