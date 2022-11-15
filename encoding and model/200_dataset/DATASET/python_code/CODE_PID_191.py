def fun191(string):
    length = len(string)
    count = 0
    for i in range(length):
        ascii = ord(string[i])
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            count = count + 1

    if count > 0:
        return 'Present'
    else:
        return 'Not Present'