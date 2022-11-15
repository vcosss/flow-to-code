def fun155(string):
    length = len(string)
    new = ''
    i = 0
    while i < length:
        ch = ord(string[i])
        if ch >= 97 and ch <= 122:
            new = new + chr(ch - 32)
        else:
            new = new + chr(ch)
        i = i + 1

    return new