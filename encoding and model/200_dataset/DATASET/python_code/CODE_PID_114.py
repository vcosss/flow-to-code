def fun114(num1, num2):
    hcf = 0
    limit = min(num1, num2)
    for i in range(1, limit+1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    
    return hcf