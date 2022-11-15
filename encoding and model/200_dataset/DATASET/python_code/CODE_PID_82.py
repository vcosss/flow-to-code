def fun82(N):
    sum = 0
    for i in range(1, N+1):
        if i % 2 != 0:
            sum = sum + i
    return sum