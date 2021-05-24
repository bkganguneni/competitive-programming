s = input()
a = []
if len(s)<3:
    print(0)
else:
    for i in range(1,len(s)-1):
        if s[i] != "," or s[i] == '':
            a.append(s[i])
    a = a[::2]
    print(len(set(a)))