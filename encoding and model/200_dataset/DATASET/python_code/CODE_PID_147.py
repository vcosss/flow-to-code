def fun147(num, k):
    count = 0
    while num != 0:
        digit = num % 10
        if digit == k:
            count = count + 1
        num = num // 10
    
    if count > 0:
        return 'Present'
    else:
        return 'Not Present'