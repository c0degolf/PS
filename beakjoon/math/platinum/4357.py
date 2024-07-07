from math import sqrt, ceil

def BSGS(p,b,n): # b^x == n mod p
    s = set()
    k = ceil(sqrt(p))
    binvk = pow(pow(b, k, p), p - 2, p)  # by Fermat's little theorem
    t = 1

    # Baby-step
    for i in range(k):
        s.add(t)
        t = (t * b) % p

    # Giant-step
    t = 1
    for i in range(k):
        x = (n * t) % p
        if x in s:
            t = 1
            for j in range(k):
                if t == x:
                    return i * k + j
                t = (t * b) % p
        t = (t * binvk) % p
    return "no solution"

for line in open(0):
    print(BSGS(*map(int, line.split())))