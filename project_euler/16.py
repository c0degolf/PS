def sol(n): # sum of the digits of the number 2^n
    n = str(1 << n)

    s = 0
    for digit in n:
        s += int(digit)

    return s

assert sol(15) == 26

print(sol(1000))