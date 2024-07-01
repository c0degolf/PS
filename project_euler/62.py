def sol(num):
    db = {}

    i = 1
    while True:
        n = "".join(sorted([*str(i**3)]))
        try: db[n] += [i]
        except: db[n] = [i]

        if len(db[n]) == num:
            return db[n][0]**3

        i += 1

assert sol(3) == 41063625

print(sol(5))