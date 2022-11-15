def fun174(string, char):
    length = len(string)
    count = 0
    for i in range(length):
        ch = string[i]
        if ch == char:
            count = count + 1
    
    return count