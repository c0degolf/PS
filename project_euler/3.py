pli = [2,3,5,7,11,13,17,19,23,29,31,37,41]

def power(x,y,p):
    if y<2: return (x**y)%p
    else:
        d = y//2
        if y%2 == 0: return (power(x,d,p)**2)%p 
        else: return (x*(power(x,d,p))**2)%p
        
def miller_rabin(n,a):
    s,d = 0,n-1
    while d%2 == 0: s += 1; d //= 2
    x = power(a,d,n)
    if x == 1 or x+1 == n: return True
    for i in range(0, s-1):
        x = power(x,2,n)
        if x+1 == n: return True
    return False
 
def isprime(n):
    if n in pli: return True
    if n == 1 or n%2 == 0: return False
    for p in pli:
        if not miller_rabin(n,p): return False
    return True

def sol(n):
    cnt, num = 0, 2
    while cnt != n:
        if isprime(num):
            cnt += 1
        num += 1
    return num-1

assert sol(6) == 13

print(sol(10001))