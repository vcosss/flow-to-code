def fun88(num, k):
    count = 0
    while num != 0:
        d = num % 10
        if d == k:
            count = count + 1
        num = num // 10

    return count
