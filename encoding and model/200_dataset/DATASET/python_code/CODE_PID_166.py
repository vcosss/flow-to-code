def fun166(string):
    length = len(string)
    count = 0
    for i in range(length):
        ascii = ord(string[i])
        if ascii == 32:
            count = count + 1

    count = count + 1
    return count