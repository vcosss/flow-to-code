def fun67(ch):
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        return 'Alphabet'
    else:
        return 'Not an alphabet'