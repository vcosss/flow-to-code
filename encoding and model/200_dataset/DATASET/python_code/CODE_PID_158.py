def fun158(string):
    length = len(string)
    count = 0
    for i in range(length):
        ascii = ord(string[i])
        if ascii >= 65 and ascii <= 90:
            count = count + 1

    return count