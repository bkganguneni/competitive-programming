from itertools import permutations
s = input()
a = sorted([''.join(i) for i in list(set(permutations(s)))])
print(len(a))
for i in a:
    print(i)