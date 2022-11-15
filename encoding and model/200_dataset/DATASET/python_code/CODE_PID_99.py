def fun99(N, k):
    sum = 0
    for i in range(1, N+1):
        if i % k == 0:
            sum = sum + i
    return sum