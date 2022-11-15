def fun115(num1, num2):
    hcf = 0
    limit = min(num1, num2)
    i = 1
    while i <= limit:
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
        i = i + 1
    
    return hcf