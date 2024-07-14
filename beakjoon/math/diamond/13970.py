import sys
from math import log2

input = sys.stdin.readline

def euler_phi(n):
    i, phi = 2, n
    while i*i <= n:
        if n%i == 0:
            phi -= phi//i
            while n%i == 0:
                n = n//i
        i += 1
    if n != 1:
        phi -= phi//n
    return phi

def calc_exp(x, y):
	if x==1 or y==0: return 1
	if x>=2 and y>=7: return MAX
	if x>=3 and y>=5: return MAX
	if x>=4 and y>=4: return MAX
	if x>=5 and y>=3: return MAX
	if x>=10 and y>=2: return MAX
	if x>=MAX and y>=1: return MAX
	return pow(x, y)

def calc(depth):
    if k-depth+1 >= 4: return MAX
    if depth == k: return primes[k]
    exp = calc_exp(primes[k-1], primes[k])
    for i in range(k-2, depth-1, -1): 
        exp = calc_exp(primes[i], exp)
    return exp
        
def solve(depth, mod):
    if mod == 1:
        return 0
    if depth == k:
        return primes[depth] % mod
    _exp = calc(depth+1)
    if _exp >= MAX:
        phi = m_phi[depth]
        exp = solve(depth+1, phi)
        return pow(primes[depth], exp + MAX*phi, mod)
    else:
        exp = _exp
        return pow(primes[depth], exp, mod)

T, M = map(int, input().split())
MAX = int(log2(M)) + 1

m_phi = [M]
while m_phi[-1] != 1:
    m_phi.append(euler_phi(m_phi[-1]))

for _ in range(T):
    k, *primes = map(int, input().split())
    
    primes = [None] + primes

    for i in range(k, 0, -1):
        if primes[i] == 1:
            k = i-1
    
    print(1 if k == 0 else solve(1, M))