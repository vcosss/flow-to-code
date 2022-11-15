def fun136(N):
    sum = 0
    i = 1
    while i <= N:
        sum = sum + i * i * i
        i = i + 1
    
    return sum