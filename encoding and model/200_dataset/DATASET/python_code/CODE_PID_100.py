def fun100(N, k):
    sum = 0
    i = 1
    while i <= N:
        if i % k == 0:
            sum = sum + i
        i = i + 1
        
    return sum