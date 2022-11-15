def fun123(a, d, N):
    term = a
    for i in range(1, N):
        term = term + d
    
    term = 1 / term
    return term 