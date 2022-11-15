def fun96(a, b):
    sum = 0
    i = a
    while i <= b:
        if i % 2 != 0:
            sum = sum + i
        i = i + 1

    return sum