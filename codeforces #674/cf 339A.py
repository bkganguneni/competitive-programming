a = list(input())
b = [int(a[i]) for i in range(0,len(a),2)]
b.sort()
for i in range(0,len(a),2):
    a[i] = str(b[i//2])
print("".join(a))
