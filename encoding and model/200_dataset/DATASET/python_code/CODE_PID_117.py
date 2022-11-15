def fun117(N):
    a = 0
    b = 1
    if N == 1:
        return a
    elif N == 2:
        return b
    else:
        for i in range(3, N+1):
            c = a + b
            a = b
            b = c
        
        return c
