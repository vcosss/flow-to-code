def fun90(num):
    res = 0
    order = 1
    while num != 0:
        rem = num % 8
        res = rem * order + res
        num = num // 8
        order = order * 10
    return res 