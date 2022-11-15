def fun200(string):
    length = len(string)
    new = ''
    i = 0
    while i < length:
        ascii = ord(string[i])
        if ascii >= 48 and ascii <= 57:
            new = new + string[i]
        i = i + 1

    return new