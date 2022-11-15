def fun95(a, b):
    sum = 0

    for i in range(a, b+1):
        if i % 2 != 0:
            sum = sum + i
    
    return sum