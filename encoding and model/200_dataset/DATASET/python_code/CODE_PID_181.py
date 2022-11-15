def fun181(string, char):
    length = len(string)
    index = -1
    i = 0
    while i < length:
        ch = string[i]
        if ch == char:
            index = i
        i = i + 1
    
    return index
