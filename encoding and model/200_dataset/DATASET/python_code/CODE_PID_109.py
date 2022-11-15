def fun109(num):
    sum = 0
    i = 1
    while i <= num:
        if num % i == 0:
            sum = sum + i
        i = i + 1

    return sum 