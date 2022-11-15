def fun128(N, k):
    term = 1
    i = 1 
    while i < N:
        term = 1 / i * k
        i = i + 1

    return term