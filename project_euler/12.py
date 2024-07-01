from sympy import factorint

def getFactor(n):
    ret = 1
    for u, v in factorint(n).items():
        ret *= v+1
    return ret

s, i = 0, 1
while True:
    s += i
    i += 1
    if getFactor(s) >= 500:
        print(s)
        break