def fun118(N):
    a = 0
    b = 1
    c = 2
    if N == 1:
        return a
    elif N == 2:
        return b
    elif N == 3:
        return c
    else:
        for i in range(4, N + 1):
            d = a + b + c
            a = b
            b = c
            c = d

        return d