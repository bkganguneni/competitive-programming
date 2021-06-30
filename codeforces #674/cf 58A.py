a=input()
h="hello"
z=0
ans="NO"
for i in a:
    if i==h[z]:
        z+=1
    if z==5:
        ans="YES"
        break
print(ans)
