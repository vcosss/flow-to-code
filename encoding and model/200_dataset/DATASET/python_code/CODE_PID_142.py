def fun142(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    
    if count == 2:
        return 'Prime Number'
    else:
        return 'Composite Number'
        