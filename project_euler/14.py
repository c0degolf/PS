def LCS(n):
    cnt = 0
    while n != 1:
        if n%2: n = 3*n + 1
        else: n = n // 2
        cnt += 1

    return cnt+1

def sol(n):
    mx = (0, 0)
    for i in range(1, n+1):
        k = LCS(i)
        if k >= mx[1]:
            mx = (i, k)
    return mx

assert LCS(13) == 10

print(sol(1000000))