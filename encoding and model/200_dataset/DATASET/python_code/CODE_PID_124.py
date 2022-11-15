def fun124(a, d, N):
    term = a
    i = 1
    while i < N:
        term = term + d
        i = i + 1
    
    term = 1 / term
    return term