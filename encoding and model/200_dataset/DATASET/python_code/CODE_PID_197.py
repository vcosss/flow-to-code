def fun197(string):
    length = len(string)
    new = ''
    for i in range(length):
        ascii = ord(string[i])
        if ascii >= 97 and ascii <= 122:
            new = new + string[i]

    return new