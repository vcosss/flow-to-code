def fun64(ch):
    ascii = ord(ch)
    if ascii >= 48 and ascii <= 57:
        return 'A Digit'
    else:
        return 'Not a Digit'