def fun199(string):
    length = len(string)
    new = ''
    for i in range(length):
        ascii = ord(string[i])
        if ascii >= 48 and ascii <= 57:
            new = new + string[i]

    return new