def primeList(n):
    arr = [1] * (n+1)
    arr[0], arr[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            arr[j] = 0
    
    return arr

def sol(n): # sum of primes below *n*
    arr = primeList(n)

    s = 0
    for i in range(1, n+1):
        if arr[i]: s += i
    
    return s

assert sol(10) == 17

print(sol(2000000))