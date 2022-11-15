def fun107(num):
    pos = 1
    nums = num
    while num != 0:
        pos = pos * 10
        num = num // 10

    pos = pos // 10
    sum = nums // pos + nums % 10
    return sum