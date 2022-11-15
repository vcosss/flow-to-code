def fun148(num):
    flag = True
    while num != 0:
        digit = num % 10
        if digit > 1:
            flag = False
        
        num = num // 10
    
    if flag == True:
        return 'Valid'
    else:
        return 'Invalid'