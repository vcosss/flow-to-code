def fun86(num):
    codd = 0
    while num != 0:
        d = num % 10
        if d % 2 != 0:
            codd = codd + 1
        num = num // 10
    
    return codd