def fun146(num):
    count = 0
    while num != 0:
        digit = num % 10
        if digit == 0:
            count = count + 1
        num = num // 10

    if count > 0:
        return 'Duck Number'
    else:
        return 'Not a Duck Number'