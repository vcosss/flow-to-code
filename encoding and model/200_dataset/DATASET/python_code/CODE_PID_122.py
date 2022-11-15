def fun122(a, r, N):
    term = a
    i = 1
    while i < N:
        term = term * r
        i = i + 1
    
    return term
    