def fun195(string):
    length = len(string)
    new = ''
    for i in range(length):
        ascii = ord(string[i])
        if ascii >= 65 and ascii <= 90:
            new = new + string[i]

    return new