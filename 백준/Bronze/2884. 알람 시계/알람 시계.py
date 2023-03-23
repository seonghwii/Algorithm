h, m = map(int, input().split())
if m < 45:
    m = 15 + m
    h = h - 1
    if h == -1 : h = 23
    print(h, m)
else:
    m = m - 45
    print(h, m)
    