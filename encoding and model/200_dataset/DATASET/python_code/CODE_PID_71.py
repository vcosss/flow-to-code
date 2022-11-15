def fun71(num):
    pro = 1
    while num != 0:
        d = num % 10
        pro = pro * d
        num = num // 10
    return pro