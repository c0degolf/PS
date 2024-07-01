from Crypto.Util.number import isPrime
from sympy import divisors, gcd, prod
from random import sample

n = 2**8 * 3**6 * 5**4 * 7**2 * 11

_n_div = list(divisors(n))
S = []

for div in _n_div:
    div = div + 1
    if isPrime(div) and gcd(div, n) == 1:
        if 10**7 <= div < 10**8:
            S.append(div)

five, six = {}, {}

def find():
    def search():
        while True:
            div = sample(S, 5)
            D = prod(div)

            try: inv = pow(D, -1, n)
            except: continue

            six[inv] = D

            if inv in six and D%n in five:
                return D * five[D%n]

            div = sample(S, 6)
            D = prod(div)

            try: inv = pow(D, -1, n)
            except: continue

            five[inv] = D

            if inv in five and D%n in six:
                return D * six[D%n]

    while True:
        sol = search()
        factors = []
        for s in S:
            if sol % s == 0:
                factors.append(s)

        if len(factors) == 11:
            return factors, sol
        
good, choco = find()

assert all([10**7 <= i < 10**8 for i in good])
assert all([(choco-1)%(i-1)==0 for i in good])
assert choco % n == 1

print(" ".join(map(str, good)))