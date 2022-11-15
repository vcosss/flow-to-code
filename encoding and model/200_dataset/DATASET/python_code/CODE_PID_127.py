def fun127(N, k):
    term = 1
    for i in range(1, N):
        term = 1 / i * k

    return term