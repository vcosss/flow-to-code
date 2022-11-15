def fun190(string):
    length = len(string)
    new = ''
    i = length - 1
    while i >= 0:
        new = new + string[i]
        i = i - 1
    
    if string == new:
        return 'Palindrome string'
    else:
        return 'Not a Palindrome string'