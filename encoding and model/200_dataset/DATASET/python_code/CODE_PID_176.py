def fun176(string, char):
    length = len(string)
    count = 0
    for i in range(length):
        ch = string[i]
        if ch == char:
            count = count + 1
    
    if count > 0:
        return 'Present'
    else:
        return 'Not Present'