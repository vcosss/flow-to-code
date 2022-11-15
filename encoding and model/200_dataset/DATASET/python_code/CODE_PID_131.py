def fun131(N, k):
    term = 1
    sum = 0
    for i in range(1, N):
        sum = sum + term
        term = 1 / i * k

    return sum