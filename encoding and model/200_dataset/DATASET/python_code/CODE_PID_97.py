def fun97(a, b, k):
    sum = 0
    for i in range(a, b+1):
        if i % k == 0:
            sum = sum + i

    return sum