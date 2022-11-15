def fun192(string):
    length = len(string)
    count = 0
    i = 0
    while i < length:
        ascii = ord(string[i])
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            count = count + 1
        
        i = i + 1

    if count > 0:
        return 'Present'
    else:
        return 'Not Present'