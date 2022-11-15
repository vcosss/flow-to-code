def fun202(N):
    a = 0
    b = 1
    if N == 1:
        return a
    elif N == 2:
        return b
    else:
        i = 3
        while i <= N:
            c = a + b
            a = b
            b = c
            i = i + 1
        
        return c
