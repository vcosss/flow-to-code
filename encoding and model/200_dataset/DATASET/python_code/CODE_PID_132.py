def fun132(N, k):
    term = 1
    sum = 0
    i = 1 
    while i < N:
        sum = sum + term
        term = 1 / i * k
        i = i + 1

    return sum