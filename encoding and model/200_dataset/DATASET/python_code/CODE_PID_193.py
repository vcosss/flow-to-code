def fun193(string):
    length = len(string)
    count = 0
    for i in range(length):
        ascii = ord(string[i])
        if ascii >= 48 and ascii <= 57:
            count = count + 1

    if count > 0:
        return 'Present'
    else:
        return 'Not Present'