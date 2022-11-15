def fun84(num):
    rev = 0
    while num != 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    return rev