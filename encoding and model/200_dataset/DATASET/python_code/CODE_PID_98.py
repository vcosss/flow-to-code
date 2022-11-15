def fun98(a, b, k):
    sum = 0
    i = a
    while i <= b:
        if i % k == 0:
            sum = sum + i
        i = i + 1

    return sum