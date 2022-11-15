def fun135(N):
    sum = 0
    for i in range(1, N+1):
        sum = sum + i * i * i

    return sum