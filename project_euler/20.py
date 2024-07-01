from math import factorial

def sol(n):
    n = str(factorial(n))

    s = 0
    for digit in n:
        s += int(digit)

    return s

assert sol(10) == 27

print(sol(100))