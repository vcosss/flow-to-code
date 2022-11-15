def fun189(string):
    length = len(string)
    new = ''
    for i in range(length - 1, -1, -1):
        new = new + string[i]
    

    if string == new:
        return 'Palindrome string'
    else:
        return 'Not a Palindrome string'
