u, v = 0, 1
cnt = 0
while u < 4000000:
    u, v = u+v, u
    cnt += 1
print(cnt)