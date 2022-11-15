def fun140(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    
    if sum == num:
        return 'Perfect Number'
    else:
        return 'Not a Perfect Number'