def fun152(string):
    length = len(string)
    new = ''
    for i in range(length):
        ch = ord(string[i])
        if ch >= 65 and ch <= 90:
            new = new + chr(ch + 32)
        else:
            new = new + chr(ch)
    
    return new
