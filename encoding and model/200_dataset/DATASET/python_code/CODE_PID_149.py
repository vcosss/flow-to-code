def fun149(num):
    flag = True
    while num != 0:
        digit = num % 10
        if digit > 7:
            flag = False
        
        num = num // 10
    
    if flag == True:
        return 'Valid'
    else:
        return 'Invalid'