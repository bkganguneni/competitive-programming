a=int(input())
ans="NO"
for i in [4,7,47,74,447,474,477]:
    if a%i==0:
        ans="YES"
        break
print(ans)
