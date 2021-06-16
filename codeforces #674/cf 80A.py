def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out
n,m = map(int,input().split())
out = primes(m)
if n==out[-1]:
    print("NO")
else:
    if n in out and m in out and (out.index(m)-out.index(n))==1:
        print("YES")
    else:
        print("NO")
