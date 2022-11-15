def fun169(string):
    length = len(string)
    count = 0
    i = 0
    while i < length:
        ch = string[i]
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count = count + 1
        i = i + 1
    
    return count
