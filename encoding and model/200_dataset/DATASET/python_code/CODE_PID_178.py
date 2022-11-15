def fun178(string, char):
    length = len(string)
    index = -1
    for i in range(length-1, -1, -1):
        ch = string[i]
        if ch == char:
            index = i
    
    return index
