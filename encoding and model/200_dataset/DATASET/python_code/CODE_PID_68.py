def fun68(ch):
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii <= 57):
        return 'Not a Special Character'
    else:
        return 'Special Character'