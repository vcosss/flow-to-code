def fun196(string):
    length = len(string)
    new = ''
    i = 0
    while i < length:
        ascii = ord(string[i])
        if ascii >= 65 and ascii <= 90:
            new = new + string[i]
        i = i + 1

    return new