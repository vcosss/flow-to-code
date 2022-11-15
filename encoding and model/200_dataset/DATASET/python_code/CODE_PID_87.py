def fun87(num):
    ceven = 0
    while num != 0:
        d = num % 10
        if d % 2 == 0:
            ceven = ceven + 1
        num = num // 10
    
    return ceven 
        