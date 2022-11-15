def fun106(a, d, N):
    sum = 0
    term = a
    i = 1
    while i <= N:
        sum = sum + 1 / term
        term = term + d
        i = i + 1

    return sum