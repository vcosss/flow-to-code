def fun102(a, d, N):
    sum = 0
    term = a
    i = 1
    while i <= N:
        sum = sum + term
        term = term + d
        i = i + 1
        
    return sum