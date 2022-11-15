def fun173(string):
    length = len(string)
    new = ''
    i = length - 1
    while i >= 0:
        new = new + string[i]
        i = i - 1
    
    return new