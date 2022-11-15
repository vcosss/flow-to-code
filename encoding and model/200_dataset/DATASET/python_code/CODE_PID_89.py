def fun89(num):
    res = 0
    order = 1
    while num != 0:
        rem = num % 2
        res = rem * order + res
        num = num // 2
        order = order * 10
    return res 