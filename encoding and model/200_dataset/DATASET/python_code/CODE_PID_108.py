def fun108(num):
    sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            sum = sum + i
    
    return sum