def fun179(string, char):
    length = len(string)
    index = -1
    i = length - 1
    while i >= 0:
        ch = string[i]
        if ch == char:
            index = i
        i = i - 1
    
    return index
