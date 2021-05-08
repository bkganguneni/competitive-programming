s = list(input())
count = 0
max = 0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count = count+1
        if max<=count:
            max = count
    elif s[i]!=s[i+1]:
        count = 0
print(max+1)