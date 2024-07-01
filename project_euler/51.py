from sympy import nextprime, isprime
from itertools import combinations

def findSubPrime(n):
    q = 2
    while True:
        p = [*str(q)]
        k = len(p)
        comb = []
        for i in range(1, k+1):
            comb += list(combinations(range(k), i))
        for com in comb:
            cnt, arr = 0, []

            for i in range(1 if (0 in com) else 0, 10):
                pp = p[:]
                for c in com:
                    pp[c] = str(i)
                pp = int("".join(pp))
                if isprime(pp):
                    cnt += 1
                    arr.append(pp)
            if cnt == n and q in arr:
                assert min(arr) == q
                assert len(arr) == n
                return q
        q = nextprime(q)

print(findSubPrime(8))