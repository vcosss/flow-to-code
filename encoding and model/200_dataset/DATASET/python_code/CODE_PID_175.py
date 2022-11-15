def fun175(string, char):
    length = len(string)
    count = 0
    i = 0
    while i < length:
        ch = string[i]
        if ch == char:
            count = count + 1
        i = i + 1
    
    return count