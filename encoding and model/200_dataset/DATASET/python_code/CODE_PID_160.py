def fun160(string):
    length = len(string)
    count = 0
    for i in range(length):
        ascii = ord(string[i])
        if ascii >= 97 and ascii <= 122:
            count = count + 1

    return count