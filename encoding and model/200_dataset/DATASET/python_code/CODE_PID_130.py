def fun130(N):
    term = 1
    sum = 0
    i = 1 
    while i < N:
        sum = sum + term
        term = term * 10 + 1
        i = i + 1
    
    return sum