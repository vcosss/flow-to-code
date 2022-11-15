def fun129(N):
    term = 1
    sum = 0
    for i in range(1, N):
        sum = sum + term
        term = term * 10 + 1
    
    return sum
