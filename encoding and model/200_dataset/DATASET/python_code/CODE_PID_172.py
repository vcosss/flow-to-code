def fun172(string):
    length = len(string)
    new = ''
    for i in range(length - 1, -1, -1):
        new = new + string[i]
    
    return new
