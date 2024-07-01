for a in range(1, 1000//3):
    for b in range(a+1, (1000-a)//2):
        c = 1000 - a - b

        assert a+b+c == 1000
        assert a < b < c

        if a**2 + b**2 == c**2:
            exit(f"{a = } {b = } {c = }\n{a + b + c = }\n{a * b * c = }")