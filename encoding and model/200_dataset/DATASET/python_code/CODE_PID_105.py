def fun105(a, d, N):
    sum = 0
    term = a
    for i in range(1, N+1):
        sum = sum + 1 / term
        term = term + d
    
    return sum