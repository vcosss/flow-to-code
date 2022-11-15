def fun151(num):
    count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            count = count + 1
        i = i + 1
    
    return count