def fun153(string):
    length = len(string)
    new = ''
    i = 0
    while i < length:
        ch = ord(string[i])
        if ch >= 65 and ch <= 90:
            new = new + chr(ch + 32)
        else:
            new = new + chr(ch)
        i = i + 1

    return new