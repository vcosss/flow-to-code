def fun85(num):
    t = 1
    nums = num
    while num != 0:
        t = t * 10
        num = num // 10
    t = t // 10
    mdigit = nums // t
    return mdigit