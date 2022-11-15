def fun104(a, r, N):
    sum = 0
    term = a
    i = 1
    while i <= N:
        sum = sum + term
        term = term * r
        i = i + 1
    
    return sum