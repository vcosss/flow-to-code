def fun103(a, r, N):
    sum = 0
    term = a
    for i in range(1, N+1):
        sum = sum + term
        term = term * r
    
    return sum