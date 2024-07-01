def gcd(u, v):
    while v:
        u, v = v, u%v
    return u

def lcm(u, v):
    return u*v // gcd(u, v)

def sol(n): # evenly devisible by 1 to n
    num = 1
    for i in range(2, n+1):
        num = lcm(num, i)
    return num

assert sol(10) == 2520

print(sol(20))