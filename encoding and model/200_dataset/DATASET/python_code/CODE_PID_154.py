def fun154(string):
    length = len(string)
    new = ''
    for i in range(length):
        ch = ord(string[i])
        if ch >= 97 and ch <= 122:
            new = new + chr(ch - 32)
        else:
            new = new + chr(ch)
    
    return new
