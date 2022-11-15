def fun180(string, char):
    length = len(string)
    index = -1
    for i in range(length):
        ch = string[i]
        if ch == char:
            index = i
    
    return index
