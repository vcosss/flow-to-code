def fun170(string):
    length = len(string)
    count = 0
    for i in range(length):
        ch = string[i]
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count = count + 1
    
    count = length - count
    
    return count