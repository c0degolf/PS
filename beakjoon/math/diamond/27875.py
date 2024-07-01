"""
SAGEMATH == GOD

solve.sage;
print((pi*pi).n(digits=378300).hex()[int(input()-1)]) << that's all! what a beautiful language!
"""

def S(j, n):
    s = 0.0
    for k in range(n+1):
        r = 8*k+j
        s = (s + float(pow(16, n-k, r*r)) / float(r*r)) % 1.0

    t = 0.0
    k = n + 1
    while 1:
        r = 8*k+j
        newt = t + pow(16, n-k) / (r*r)
        if t == newt:
            break
        else:
            t = newt
        k += 1
    return s + t

def pi(n):
    n -= 1
    x = (16*S(1, n) - 16*S(2, n) - 8*S(3, n) - 16*S(4, n) - 4*S(5, n) - 4*S(6, n) + 2*S(7, n)) % 1.0
    return "%X" % (int(x * (1 << 56)) >> 52)

print(pi(int(input())))