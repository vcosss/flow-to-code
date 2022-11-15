def fun53(len1, len2, len3):
    if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
        return 'VALID TRIANGLE'
    else:
        return 'NOT A VALID TRIANGLE' 