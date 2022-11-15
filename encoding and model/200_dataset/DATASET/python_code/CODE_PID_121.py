def fun121(a, r, N):
    term = a
    for i in range(1, N):
        term = term * r

    return term
