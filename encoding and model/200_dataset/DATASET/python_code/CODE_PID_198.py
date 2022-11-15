def fun198(string):
    length = len(string)
    new = ''
    i = 0
    while i < length:
        ascii = ord(string[i])
        if ascii >= 97 and ascii <= 122:
            new = new + string[i]
        i = i + 1

    return new