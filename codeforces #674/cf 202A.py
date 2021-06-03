s = list(input())
s.sort()
a = ""
if s.count(s[-1])<=1:
    print(s[-1])
else:
    s = s[len(s)-s.count(s[-1]):]
    for i in range(len(s)):
        a = a+s[i]
    print(a)
    
