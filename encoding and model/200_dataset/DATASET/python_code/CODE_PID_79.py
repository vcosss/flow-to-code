def fun79(N):
    sum = 0
    i = 1
    while i <= N:
        if i % 2 == 0:
            sum = sum + i
        i = i + 1
    return sum